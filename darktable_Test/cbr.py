import base64
import json
import re
import struct
import zlib
import sys
from typing import Any, Dict, List


# ====== darktable 5.4.0 colorbalancergb layout ======
FIELD_ORDER_32F: List[str] = [
    "shadows_Y","shadows_C","shadows_H",
    "midtones_Y","midtones_C","midtones_H",
    "highlights_Y","highlights_C","highlights_H",
    "global_Y","global_C","global_H",
    "shadows_weight","white_fulcrum","highlights_weight",
    "chroma_shadows","chroma_highlights","chroma_global","chroma_midtones",
    "saturation_global","saturation_highlights","saturation_midtones","saturation_shadows",
    "hue_angle",
    "brilliance_global","brilliance_highlights","brilliance_midtones","brilliance_shadows",
    "mask_grey_fulcrum",
    "vibrance","grey_fulcrum","contrast",
]
ENUM_FIELD = "saturation_formula"

DEFAULTS: Dict[str, Any] = {k: 0.0 for k in FIELD_ORDER_32F}
DEFAULTS[ENUM_FIELD] = 1


def json_to_gz03_colorbalancergb(obj: Dict[str, Any]) -> str:
    allowed = set(FIELD_ORDER_32F) | {ENUM_FIELD}
    unknown = sorted(k for k in obj.keys() if k not in allowed)
    if unknown:
        raise ValueError(f"Unknown keys in JSON: {unknown}")

    floats: List[float] = []
    for k in FIELD_ORDER_32F:
        v = obj.get(k, DEFAULTS[k])
        try:
            floats.append(float(v))
        except Exception as e:
            raise ValueError(f"Field '{k}' must be numeric, got {v!r}") from e

    enum_val = obj.get(ENUM_FIELD, DEFAULTS[ENUM_FIELD])
    try:
        enum_i32 = int(enum_val)
    except Exception as e:
        raise ValueError(f"Field '{ENUM_FIELD}' must be int, got {enum_val!r}") from e

    raw = struct.pack("<32f", *floats) + struct.pack("<i", enum_i32)
    comp = zlib.compress(raw, level=9)
    return "gz03" + base64.b64encode(comp).decode("ascii")


def patch_xmp_text(xmp_in: str, xmp_out: str, new_params: str) -> None:
    # Read as text, preserving original newlines as-is
    with open(xmp_in, "r", encoding="utf-8", newline="") as f:
        s = f.read()

    # 1) Find the <rdf:li ...> block that contains darktable:operation="colorbalancergb"
    #    We match one rdf:li start tag (self-closing or not); your sample uses self-closing "/>"
    #    The pattern is non-greedy across lines.
    li_pat = re.compile(
        r'(<rdf:li\b[^>]*\bdarktable:operation="colorbalancergb"[^>]*>)',
        flags=re.IGNORECASE | re.DOTALL,
    )

    m = li_pat.search(s)
    if not m:
        raise RuntimeError('Cannot find <rdf:li ... darktable:operation="colorbalancergb" ...> in XMP')

    li_tag = m.group(1)

    # 2) Replace darktable:params="..."
    #    Keep the quote style consistent (assumes double quotes as in your file).
    params_pat = re.compile(r'(darktable:params=")([^"]*)(")', flags=re.DOTALL)
    if not params_pat.search(li_tag):
        raise RuntimeError('Found colorbalancergb rdf:li, but no darktable:params="..." attribute inside it')

    new_li_tag = params_pat.sub(rf'\1{new_params}\3', li_tag, count=1)

    # 3) Splice back into the full document
    s2 = s[:m.start(1)] + new_li_tag + s[m.end(1):]

    # Write out (preserve newlines)
    with open(xmp_out, "w", encoding="utf-8", newline="") as f:
        f.write(s2)


def main() -> int:
    # Defaults
    json_path = "colorbalancergb.json"
    xmp_in = "sunset.xmp"
    xmp_out = "sunset.patched.xmp"

    # Usage:
    # python3 cbr_patch_text.py [xmp_in] [json_path] [xmp_out]
    if len(sys.argv) >= 2:
        xmp_in = sys.argv[1]
    if len(sys.argv) >= 3:
        json_path = sys.argv[2]
    if len(sys.argv) >= 4:
        xmp_out = sys.argv[3]

    with open(json_path, "r", encoding="utf-8") as f:
        obj = json.load(f)

    new_params = json_to_gz03_colorbalancergb(obj)
    patch_xmp_text(xmp_in, xmp_out, new_params)

    print(f"Patched file: {xmp_out}")
    print(f"Updated darktable:params (colorbalancergb) to: {new_params}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
