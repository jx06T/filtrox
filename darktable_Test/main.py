#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import base64
import ctypes
import json
import re
import sys
import zlib
from ctypes import c_float, c_int32
from typing import Any, Dict, Optional, Tuple
from src_gmic.ai_engine import AIEngine, load_engine_from_env

# =========================
# Fixed format rules (based on your sample XMP)
# =========================
HEX_OPS = {"exposure", "sigmoid", "toneequal"}  # IMPORTANT: tone equalizer = toneequal


def dt_encode_gz(raw: bytes, level: int = 9) -> str:
    comp = zlib.compress(raw, level=level)
    clen = len(comp)
    if clen == 0:
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
    # default: follow fixed rules
    if op in HEX_OPS:
        return raw.hex()
    return dt_encode_gz(raw)


# =========================
# Robust: find ONLY the start tag of rdf:li (multiline OK)
# =========================
def read_text_keep_newlines(path: str) -> str:
    with open(path, "r", encoding="utf-8-sig", newline="") as f:
        return f.read()


def write_text_keep_newlines(path: str, s: str) -> None:
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(s)


def find_rdf_li_start_tag(doc: str, operation: str) -> Optional[Tuple[int, int, str]]:
    """
    Returns (start_idx, end_idx, tag_text) where tag_text is from '<rdf:li' up to the first '>'.

    Works for BOTH:
      <rdf:li ... />
      <rdf:li ... >
        ...
      </rdf:li>

    Handles multiline attributes.
    """
    op = re.escape(operation)
    # Capture the whole start tag ending at the first '>'
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


def patch_operation(doc: str, operation: str, enabled: Optional[int],
                    modversion: Optional[int], params: Optional[str]) -> Tuple[str, bool]:
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


# =========================
# ctypes structs (same as before)
# =========================
CHANNEL_SIZE = 4

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

class ChannelMixerRGBParams(ctypes.Structure):
    _fields_ = [
        ("red", c_float * CHANNEL_SIZE),
        ("green", c_float * CHANNEL_SIZE),
        ("blue", c_float * CHANNEL_SIZE),
        ("saturation", c_float * CHANNEL_SIZE),
        ("lightness", c_float * CHANNEL_SIZE),
        ("grey", c_float * CHANNEL_SIZE),

        ("normalize_R", c_int32),
        ("normalize_G", c_int32),
        ("normalize_B", c_int32),
        ("normalize_sat", c_int32),
        ("normalize_light", c_int32),
        ("normalize_grey", c_int32),

        ("illuminant", c_int32),
        ("illum_fluo", c_int32),
        ("illum_led", c_int32),
        ("adaptation", c_int32),

        ("x", c_float),
        ("y", c_float),
        ("temperature", c_float),
        ("gamut", c_float),

        ("clip", c_int32),
        ("version", c_int32),
    ]

# filmicrgb: gz in your sample, but struct is build-sensitive. Prefer params_gz passthrough.
class FilmicRGBParams(ctypes.Structure):
    _fields_ = [
        ("grey_point_source", c_float),
        ("black_point_source", c_float),
        ("white_point_source", c_float),
        ("reconstruct_threshold", c_float),
        ("reconstruct_feather", c_float),
        ("reconstruct_bloom_vs_details", c_float),
        ("reconstruct_grey_vs_color", c_float),
        ("reconstruct_structure_vs_texture", c_float),
        ("security_factor", c_float),
        ("grey_point_target", c_float),
        ("black_point_target", c_float),
        ("white_point_target", c_float),
        ("output_power", c_float),
        ("latitude", c_float),
        ("contrast", c_float),
        ("saturation", c_float),
        ("balance", c_float),
        ("noise_level", c_float),

        ("preserve_color", c_int32),
        ("version", c_int32),
        ("auto_hardness", c_int32),
        ("custom_grey", c_int32),
        ("high_quality_reconstruction", c_int32),
        ("noise_distribution", c_int32),
        ("shadows", c_int32),
        ("highlights", c_int32),
        ("compensate_icc_black", c_int32),
        ("spline_version", c_int32),
        ("enable_highlight_reconstruction", c_int32),
    ]


OP_TO_STRUCT = {
    "exposure": ExposureParams,
    "filmicrgb": FilmicRGBParams,
    "sigmoid": SigmoidParams,
    "toneequal": ToneEqualParams,
    "colorbalancergb": ColorBalanceRGBParams,
    "colorequal": ColorEqualParams,
    "channelmixerrgb": ChannelMixerRGBParams,
}


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
                    cur[i] = float(v[i])
            else:
                if field_type is c_float:
                    setattr(st, field_name, float(v))
                else:
                    setattr(st, field_name, int(v))
        except Exception:
            continue


def build_params_string(op: str, mcfg: Dict[str, Any]) -> Optional[str]:
    # passthrough overrides
    if isinstance(mcfg.get("params_gz"), str) and mcfg["params_gz"].startswith("gz"):
        return mcfg["params_gz"]
    if isinstance(mcfg.get("params_hex"), str):
        return mcfg["params_hex"].lower()

    params = mcfg.get("params")
    if not isinstance(params, dict):
        return None

    st_cls = OP_TO_STRUCT.get(op)
    if st_cls is None:
        return None

    st = st_cls()
    fill_struct(st, params)
    raw = bytes(st)

    # Optional size sanity (do NOT crash whole run)
    expected = mcfg.get("_expected_bytes")
    if isinstance(expected, int) and expected > 0 and len(raw) != expected:
        # skip writing params if layout mismatch
        return None

    force_format = mcfg.get("format")  # "hex" / "gz" / None
    if force_format not in (None, "hex", "gz"):
        force_format = None

    return encode_params(op, raw, force_format=force_format)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--xmp-in", required=True)
    ap.add_argument("--xmp-out", required=True)
    ap.add_argument("--json", required=True)
    ap.add_argument("--quiet", action="store_true")
    args = ap.parse_args()

    try:
        doc = read_text_keep_newlines(args.xmp_in)
    except Exception as e:
        print(f"[ERR] read xmp failed: {e}", file=sys.stderr)
        return 2

    try:
        cfg = json.load(open(args.json, "r", encoding="utf-8"))
    except Exception as e:
        print(f"[ERR] read json failed: {e}", file=sys.stderr)
        return 2

    modules = cfg.get("modules", cfg)
    if not isinstance(modules, dict):
        print("[ERR] json must be an object (or contain 'modules' object)", file=sys.stderr)
        return 2

    patched, not_found = [], []

    for op, mcfg in modules.items():
        if not isinstance(mcfg, dict):
            not_found.append(op)
            continue

        enabled = mcfg.get("enabled")
        modversion = mcfg.get("modversion")
        enabled_val = int(enabled) if isinstance(enabled, (int, float, bool)) else None
        modversion_val = int(modversion) if isinstance(modversion, (int, float)) else None

        params_str = None
        try:
            params_str = build_params_string(op, mcfg)
        except Exception as e:
            # never abort; just skip this module
            if not args.quiet:
                print(f"[WARN] {op}: build params failed, skipped ({e})")
            params_str = None

        doc2, ok = patch_operation(doc, op, enabled_val, modversion_val, params_str)
        doc = doc2
        if ok:
            patched.append(op)
        else:
            not_found.append(op)

    try:
        write_text_keep_newlines(args.xmp_out, doc)
    except Exception as e:
        print(f"[ERR] write xmp failed: {e}", file=sys.stderr)
        return 2

    if not args.quiet:
        print("[OK] wrote:", args.xmp_out)
        print("[OK] patched:", ", ".join(patched) if patched else "(none)")
        print("[WARN] not found:", ", ".join(not_found) if not_found else "(none)")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())

