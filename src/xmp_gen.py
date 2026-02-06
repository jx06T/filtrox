#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
darktable XMP patcher (dt 5.4.x style)

- Reads a JSON config with module structs (or params_hex / params_gz passthrough)
- Patches matching <rdf:li ... darktable:operation="..."> tags in the XMP history
- Optionally inserts missing operations at the end of history

Tested to be robust against:
- UTF-8 BOM (<?xml ...?> preceded by BOM/whitespace)
- multiline <rdf:li .../> tags
"""

import argparse
import base64
import ctypes
import json
import os
import re
import sys
import zlib
from ctypes import c_float, c_int32
from typing import Any, Dict, Optional, Tuple, List


# ==========
# Encoding rules (based on your samples)
# ==========
HEX_OPS = {
    "exposure",
    "sigmoid",
    "toneequal",
    "temperature",
    "diffuse",
    "hazeremoval",
    "vignette",
    "grain",
}


def dt_encode_gz(raw: bytes, level: int = 9) -> str:
    comp = zlib.compress(raw, level=level)
    clen = len(comp)
    if clen <= 0:
        raise ValueError("zlib produced empty output")
    factor = min((len(raw) // clen) + 1, 99)
    return f"gz{factor:02d}" + base64.b64encode(comp).decode("ascii")


def encode_params(op: str, raw: bytes, force_format: Optional[str] = None) -> str:
    """
    force_format: "hex" | "gz" | None
    """
    if force_format == "hex":
        return raw.hex()
    if force_format == "gz":
        return dt_encode_gz(raw)

    if op in HEX_OPS:
        return raw.hex()
    return dt_encode_gz(raw)


# ==========
# File utils
# ==========
def read_text_keep_newlines(path: str) -> str:
    # utf-8-sig strips BOM if present (fixes "XML declaration not at start")
    with open(path, "r", encoding="utf-8-sig", newline="") as f:
        return f.read()


def write_text_keep_newlines(path: str, s: str) -> None:
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(s)


def read_json_allow_fenced(path: str) -> Dict[str, Any]:
    text = read_text_keep_newlines(path)
    fenced = re.search(r"```(?:json)?\s*(.*?)\s*```", text, flags=re.DOTALL | re.IGNORECASE)
    if fenced:
        text = fenced.group(1)
    return json.loads(text)


# ==========
# XMP tag editing
# ==========
def find_rdf_li_start_tag(doc: str, operation: str) -> Optional[Tuple[int, int, str]]:
    """
    Returns (start_idx, end_idx, tag_text) where tag_text is from '<rdf:li' up to the first '>'.
    Handles multiline attributes.
    """
    op = re.escape(operation)
    pat = re.compile(
        rf'(<rdf:li\b[^>]*\bdarktable:operation=(["\']){op}\2[^>]*>)',
        flags=re.DOTALL
    )
    m = pat.search(doc)
    if not m:
        return None
    return m.start(1), m.end(1), m.group(1)


def replace_or_insert_attr(tag: str, attr: str, value: str) -> str:
    """
    Replace attr="..." or attr='...' in a single start tag.
    If missing, insert before final '>' (preserving '/>' if present).
    """
    pat = re.compile(rf'(\s{re.escape(attr)}=)(["\'])(.*?)(\2)', flags=re.DOTALL)
    if pat.search(tag):
        return pat.sub(lambda m: m.group(1) + m.group(2) + value + m.group(4), tag, count=1)

    # insert before closing '>'
    if tag.endswith("/>"):
        return tag[:-2] + f' {attr}="{value}"' + "/>"
    if tag.endswith(">"):
        return tag[:-1] + f' {attr}="{value}"' + ">"
    return tag


def patch_operation(doc: str, operation: str,
                    enabled: Optional[int],
                    modversion: Optional[int],
                    params: Optional[str]) -> Tuple[str, bool]:
    found = find_rdf_li_start_tag(doc, operation)
    if not found:
        return doc, False

    s, e, tag = found
    new_tag = tag

    if enabled is not None:
        new_tag = replace_or_insert_attr(new_tag, "darktable:enabled", str(int(enabled)))
    if modversion is not None:
        new_tag = replace_or_insert_attr(new_tag, "darktable:modversion", str(int(modversion)))
    if params is not None:
        new_tag = replace_or_insert_attr(new_tag, "darktable:params", params)

    return doc[:s] + new_tag + doc[e:], True


def _find_history_seq_bounds(doc: str) -> Optional[Tuple[int, int]]:
    """
    Return (insert_pos, end_pos) where insert_pos is right before </rdf:Seq> of <darktable:history>.
    """
    # Find <darktable:history> ... <rdf:Seq> ... </rdf:Seq> ... </darktable:history>
    m = re.search(r"<darktable:history>\s*<rdf:Seq>(.*?)</rdf:Seq>\s*</darktable:history>",
                  doc, flags=re.DOTALL)
    if not m:
        return None
    # insert before the closing </rdf:Seq> within that match
    full = m.group(0)
    inner = m.group(1)
    start = m.start(0)
    # position of </rdf:Seq> inside doc:
    end_seq = doc.find("</rdf:Seq>", start)
    if end_seq < 0:
        return None
    return end_seq, end_seq


def _get_next_history_num(doc: str) -> int:
    nums = [int(x) for x in re.findall(r'darktable:num="(\d+)"', doc)]
    return (max(nums) + 1) if nums else 0


def _set_history_end(doc: str, new_end: int) -> str:
    # history_end is in rdf:Description attributes
    pat = re.compile(r'(darktable:history_end=")(\d+)(")')
    if pat.search(doc):
        return pat.sub(rf"\g<1>{new_end}\g<3>", doc, count=1)
    return doc


def _first_li_template(doc: str) -> Optional[str]:
    """
    Grab the first <rdf:li .../> start tag as a template for insertion.
    """
    m = re.search(r'(<rdf:li\b[^>]*?/>)', doc, flags=re.DOTALL)
    return m.group(1) if m else None


def insert_operation(doc: str, operation: str,
                     enabled: Optional[int],
                     modversion: Optional[int],
                     params: Optional[str]) -> Tuple[str, bool]:
    bounds = _find_history_seq_bounds(doc)
    tpl = _first_li_template(doc)
    if not bounds or not tpl:
        return doc, False

    num = _get_next_history_num(doc)
    tag = tpl

    tag = replace_or_insert_attr(tag, "darktable:num", str(num))
    tag = replace_or_insert_attr(tag, "darktable:operation", operation)
    tag = replace_or_insert_attr(tag, "darktable:multi_name", "")
    tag = replace_or_insert_attr(tag, "darktable:multi_name_hand_edited", "0")
    tag = replace_or_insert_attr(tag, "darktable:multi_priority", "0")

    if enabled is not None:
        tag = replace_or_insert_attr(tag, "darktable:enabled", str(int(enabled)))
    if modversion is not None:
        tag = replace_or_insert_attr(tag, "darktable:modversion", str(int(modversion)))
    if params is not None:
        tag = replace_or_insert_attr(tag, "darktable:params", params)

    insert_pos, _ = bounds
    # keep indentation similar to existing history items
    tag = "\n     " + tag.strip() + "\n"
    doc2 = doc[:insert_pos] + tag + doc[insert_pos:]

    # history_end is last_num + 1
    doc2 = _set_history_end(doc2, num + 1)
    return doc2, True


# ==========
# ctypes structs
# ==========

class ExposureParams(ctypes.Structure):
    _fields_ = [
        ("mode", c_int32),
        ("black", c_float),
        ("exposure", c_float),
        ("deflicker_percentile", c_float),
        ("deflicker_target_level", c_float),
        ("compensate_exposure_bias", c_int32),
        ("compensate_hilite_pres", c_int32),
    ]


class SigmoidParams(ctypes.Structure):
    _fields_ = [
        ("middle_grey_contrast", c_float),
        ("contrast_skewness", c_float),
        ("display_white_target", c_float),
        ("display_black_target", c_float),
        ("color_processing", c_int32),
        ("hue_preservation", c_float),
        ("red_inset", c_float),
        ("red_rotation", c_float),
        ("green_inset", c_float),
        ("green_rotation", c_float),
        ("blue_inset", c_float),
        ("blue_rotation", c_float),
        ("purity", c_float),
        ("base_primaries", c_int32),
    ]


class ToneEqualParams(ctypes.Structure):
    _fields_ = [
        ("noise", c_float),
        ("ultra_deep_blacks", c_float),
        ("deep_blacks", c_float),
        ("blacks", c_float),
        ("shadows", c_float),
        ("midtones", c_float),
        ("highlights", c_float),
        ("whites", c_float),
        ("speculars", c_float),
        ("blending", c_float),
        ("smoothing", c_float),
        ("feathering", c_float),
        ("quantization", c_float),
        ("contrast_boost", c_float),
        ("exposure_boost", c_float),
        ("details", c_int32),
        ("method", c_int32),
        ("iterations", c_int32),
    ]


class TemperatureParams(ctypes.Structure):
    _fields_ = [
        ("red", c_float),
        ("green", c_float),
        ("blue", c_float),
        ("various", c_float),   # JSON 可不提供，預設 0.0
        ("preset", c_int32),
    ]


# ---- diffuse ----
# 直接照你 JSON 欄位順序建 layout：3 ints + 12 floats = 60 bytes
class DiffuseParams(ctypes.Structure):
    _fields_ = [
        ("iterations", c_int32),
        ("sharpness", c_float),
        ("radius", c_int32),
        ("regularization", c_float),
        ("variance_threshold", c_float),
        ("anisotropy_first", c_float),
        ("anisotropy_second", c_float),
        ("anisotropy_third", c_float),
        ("anisotropy_fourth", c_float),
        ("threshold", c_float),
        ("first", c_float),
        ("second", c_float),
        ("third", c_float),
        ("fourth", c_float),
        ("radius_center", c_int32),
    ]


# ---- hazeremoval ----
# 4 floats + 2 ints = 24 bytes
class HazeRemovalParams(ctypes.Structure):
    _fields_ = [
        ("strength", c_float),
        ("distance", c_float),
        ("slope", c_float),
        ("saturation", c_float),
        ("unbound", c_int32),
        ("iterations", c_int32),
    ]


# ---- vignette ----
# scale/falloff/brightness/saturation + center[2] + autoratio + whratio + shape = 36 bytes
class VignetteParams(ctypes.Structure):
    _fields_ = [
        ("scale", c_float),
        ("falloff_scale", c_float),
        ("brightness", c_float),
        ("saturation", c_float),
        ("center", c_float * 2),   # ✅ array
        ("autoratio", c_int32),
        ("whratio", c_float),
        ("shape", c_float),
        ("dithering", c_int32),
        ("unbound", c_int32),
    ]



# ---- grain ----
# int + 2 floats = 12 bytes（照你 JSON）
class GrainParams(ctypes.Structure):
    # 16 bytes in your sample XMP: int + 3 floats
    _fields_ = [
        ("channel", c_int32),
        ("scale", c_float),
        ("strength", c_float),
        ("midtones", c_float),
    ]
# (kept from your previous code)
class ColorBalanceRGBParams(ctypes.Structure):
    _fields_ = [
        ("shadows_Y", c_float), ("shadows_C", c_float), ("shadows_H", c_float),
        ("midtones_Y", c_float), ("midtones_C", c_float), ("midtones_H", c_float),
        ("highlights_Y", c_float), ("highlights_C", c_float), ("highlights_H", c_float),
        ("global_Y", c_float), ("global_C", c_float), ("global_H", c_float),
        ("shadows_weight", c_float), ("white_fulcrum", c_float), ("highlights_weight", c_float),
        ("chroma_shadows", c_float), ("chroma_highlights", c_float), ("chroma_global", c_float), ("chroma_midtones", c_float),
        ("saturation_global", c_float), ("saturation_highlights", c_float), ("saturation_midtones", c_float), ("saturation_shadows", c_float),
        ("hue_angle", c_float),
        ("brilliance_global", c_float), ("brilliance_highlights", c_float), ("brilliance_midtones", c_float), ("brilliance_shadows", c_float),
        ("mask_grey_fulcrum", c_float),
        ("vibrance", c_float), ("grey_fulcrum", c_float), ("contrast", c_float),
        ("saturation_formula", c_int32),
    ]


class ColorEqualParams(ctypes.Structure):
    _fields_ = [
        ("threshold", c_float),
        ("smoothing_hue", c_float),
        ("contrast", c_float),
        ("white_level", c_float),
        ("chroma_size", c_float),
        ("param_size", c_float),
        ("use_filter", c_int32),

        ("sat_red", c_float), ("sat_orange", c_float), ("sat_yellow", c_float), ("sat_green", c_float),
        ("sat_cyan", c_float), ("sat_blue", c_float), ("sat_lavender", c_float), ("sat_magenta", c_float),

        ("hue_red", c_float), ("hue_orange", c_float), ("hue_yellow", c_float), ("hue_green", c_float),
        ("hue_cyan", c_float), ("hue_blue", c_float), ("hue_lavender", c_float), ("hue_magenta", c_float),

        ("bright_red", c_float), ("bright_orange", c_float), ("bright_yellow", c_float), ("bright_green", c_float),
        ("bright_cyan", c_float), ("bright_blue", c_float), ("bright_lavender", c_float), ("bright_magenta", c_float),

        ("hue_shift", c_float),
    ]


OP_TO_STRUCT = {
    "exposure": ExposureParams,
    "sigmoid": SigmoidParams,
    "toneequal": ToneEqualParams,
    "temperature": TemperatureParams,
    "diffuse": DiffuseParams,
    "hazeremoval": HazeRemovalParams,
    "vignette": VignetteParams,
    "grain": GrainParams,
    "colorbalancergb": ColorBalanceRGBParams,
    "colorequal": ColorEqualParams,
}


def _as_float(v: Any) -> float:
    # allow "inf"/"-inf"/"nan" as strings in JSON
    if isinstance(v, str):
        return float(v.strip())
    return float(v)


def fill_struct(st: ctypes.Structure, params: Dict[str, Any]) -> None:
    for field_name, field_type in getattr(st, "_fields_", []):
        if field_name not in params:
            continue
        v = params[field_name]
        try:
            cur = getattr(st, field_name)
            if isinstance(cur, ctypes.Array):
                if not isinstance(v, list):
                    continue
                for i in range(min(len(cur), len(v))):
                    cur[i] = _as_float(v[i])
            else:
                if field_type is c_float:
                    setattr(st, field_name, _as_float(v))
                else:
                    setattr(st, field_name, int(v))
        except Exception:
            # never abort whole run
            continue


def build_params_string(op: str, mcfg: Dict[str, Any]) -> Optional[str]:
    # passthrough overrides
    if isinstance(mcfg.get("params_gz"), str) and mcfg["params_gz"].startswith("gz"):
        return mcfg["params_gz"]
    if isinstance(mcfg.get("params_hex"), str):
        return str(mcfg["params_hex"]).strip().lower()

    params = mcfg.get("params")
    if not isinstance(params, dict):
        return None

    st_cls = OP_TO_STRUCT.get(op)
    if st_cls is None:
        return None

    st = st_cls()
    fill_struct(st, params)
    raw = bytes(st)

    expected = mcfg.get("_expected_bytes")
    if isinstance(expected, int) and expected > 0 and len(raw) != expected:
        return None

    force_format = mcfg.get("format")  # "hex" / "gz" / None
    if force_format not in (None, "hex", "gz"):
        force_format = None

    return encode_params(op, raw, force_format=force_format)


def run_darktable_cli(cli: str, input_img: str, xmp_path: str, output_img: str) -> int:
    # Use list-form args on POSIX; on Windows shell=True is simpler but less safe.
    cmd = f'"{cli}" "{input_img}" "{xmp_path}" "{output_img}"'
    return os.system(cmd)


def gen(input_path, config, output_path) -> int:
    ap = argparse.ArgumentParser()

    try:
        doc = ""
        doc = read_text_keep_newlines("sunset.xmp")
    except Exception as e:
        print(f"[ERR] read xmp failed: {e}", file=sys.stderr)
        return 2

    try:
        cfg = config
    except Exception as e:
        print(f"[ERR] read json failed: {e}", file=sys.stderr)
        return 2

    modules = cfg.get("modules", cfg)
    if not isinstance(modules, dict):
        print("[ERR] json must be an object (or contain 'modules' object)", file=sys.stderr)
        return 2

    patched: List[str] = []
    inserted: List[str] = []
    not_found: List[str] = []
    skipped_params: List[str] = []

    for op, mcfg in modules.items():
        if not isinstance(mcfg, dict):
            continue

        enabled = mcfg.get("enabled")
        modversion = mcfg.get("modversion")
        enabled_val = int(enabled) if isinstance(enabled, (int, float, bool)) else None
        modversion_val = int(modversion) if isinstance(modversion, (int, float)) else None

        params_str = None
        try:
            params_str = build_params_string(op, mcfg)
        except Exception as e:
            if not True:
                print(f"[WARN] {op}: build params failed, skipped params ({e})")
            params_str = None

        if params_str is None and ("params" in mcfg or "params_hex" in mcfg or "params_gz" in mcfg):
            skipped_params.append(op)

        doc2, ok = patch_operation(doc, op, enabled_val, modversion_val, params_str)
        if ok:
            doc = doc2
            patched.append(op)
            continue

        if True:
            doc3, ok2 = insert_operation(doc, op, enabled_val, modversion_val, params_str)
            if ok2:
                doc = doc3
                inserted.append(op)
            else:
                not_found.append(op)
        else:
            not_found.append(op)

    try:
        write_text_keep_newlines("sunset_out.xmp", doc)
    except Exception as e:
        print(f"[ERR] write xmp failed: {e}", file=sys.stderr)
        return 2
    
    if True:
        print(f"[OK] wrote: {output_path}" + (" (dry-run)" if False else ""))
        if patched:
            print("[OK] patched:", ", ".join(patched))
        if inserted:
            print("[OK] inserted:", ", ".join(inserted))
        if skipped_params:
            print("[WARN] params skipped (struct/size mismatch):", ", ".join(skipped_params))
        if not_found:
            print("[WARN] operations not found:", ", ".join(not_found))

    os.system(f"darktable-cli {input_path} sunset_out.xmp {output_path}")

    return output_path


if __name__ == "__main__":
    raise SystemExit(gen())
