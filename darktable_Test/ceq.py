import argparse
import base64
import json
import struct
import zlib
import xml.etree.ElementTree as ET
from typing import Any, Dict

DT_NS = "http://darktable.sf.net/"
RDF_NS = "http://www.w3.org/1999/02/22-rdf-syntax-ns#"

def _strip_bom_and_leading_ws(raw: bytes) -> bytes:
    # Fix: "XML or text declaration not at start of entity"
    if raw.startswith(b"\xef\xbb\xbf"):  # UTF-8 BOM
        raw = raw[3:]
    return raw.lstrip()

def dt_xmp_encode_gz(data: bytes) -> str:
    """
    darktable dt_exif_xmp_encode_internal(do_compress=TRUE):
      - zlib compress
      - base64
      - prefix: "gz" + 2-digit factor where factor = min(len/comp + 1, 99) with integer division
    """
    comp = zlib.compress(data)  # default level is fine (matches common zlib behavior)
    clen = len(comp)
    if clen <= 0:
        raise ValueError("zlib compress produced empty output")

    factor = min((len(data) // clen) + 1, 99)
    b64 = base64.b64encode(comp).decode("ascii")
    return f"gz{factor:02d}{b64}"

def build_colorequal_params_bytes(cfg: Dict[str, Any]) -> bytes:
    """
    darktable 5.4.0 dt_iop_colorequal_params_t layout:
      float threshold
      float smoothing_hue
      float contrast
      float white_level
      float chroma_size
      float param_size
      gboolean use_filter   (int32)
      float sat_[8]
      float hue_[8]
      float bright_[8]
      float hue_shift
    Total: 31 floats (124 bytes) + int32 (4 bytes) = 128 bytes
    """
    def getf(key: str, default: float) -> float:
        v = cfg.get(key, default)
        return float(v)

    def getb(key: str, default: bool) -> bool:
        v = cfg.get(key, default)
        return bool(v)

    order = ["red", "orange", "yellow", "green", "cyan", "blue", "lavender", "magenta"]

    sat = cfg.get("sat", {}) or {}
    hue = cfg.get("hue", {}) or {}
    bright = cfg.get("bright", {}) or {}

    # Defaults match module defaults in darktable source
    threshold     = getf("threshold", 0.10)
    smoothing_hue = getf("smoothing_hue", 1.00)
    contrast      = getf("contrast", 0.00)
    white_level   = getf("white_level", 1.00)
    chroma_size   = getf("chroma_size", 1.50)
    param_size    = getf("param_size", 1.00)
    use_filter    = getb("use_filter", True)

    sat_vals    = [float(sat.get(k, 1.0)) for k in order]
    hue_vals    = [float(hue.get(k, 0.0)) for k in order]
    bright_vals = [float(bright.get(k, 1.0)) for k in order]

    hue_shift = getf("hue_shift", 0.0)

    # Pack little-endian
    out = bytearray()
    out += struct.pack("<6f", threshold, smoothing_hue, contrast, white_level, chroma_size, param_size)
    out += struct.pack("<i", 1 if use_filter else 0)
    out += struct.pack("<8f", *sat_vals)
    out += struct.pack("<8f", *hue_vals)
    out += struct.pack("<8f", *bright_vals)
    out += struct.pack("<f", hue_shift)

    if len(out) != 128:
        raise ValueError(f"Unexpected packed size: {len(out)} bytes (expected 128)")

    return bytes(out)

def patch_xmp_colorequal_params(xmp_in: str, xmp_out: str, new_params: str) -> None:
    raw = open(xmp_in, "rb").read()
    raw = _strip_bom_and_leading_ws(raw)

    root = ET.fromstring(raw)
    tree = ET.ElementTree(root)

    op_key = f"{{{DT_NS}}}operation"
    params_key = f"{{{DT_NS}}}params"

    found = 0
    for li in root.iter():
        if li.attrib.get(op_key) == "colorequal":
            li.set(params_key, new_params)
            found += 1

    if found == 0:
        raise RuntimeError('No history item found with darktable:operation="colorequal".')

    tree.write(xmp_out, encoding="UTF-8", xml_declaration=True)

def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--xmp-in", required=True)
    ap.add_argument("--xmp-out", required=True)
    ap.add_argument("--json", required=True)
    args = ap.parse_args()

    cfg = json.load(open(args.json, "r", encoding="utf-8"))
    params_bytes = build_colorequal_params_bytes(cfg)
    params_gz = dt_xmp_encode_gz(params_bytes)

    patch_xmp_colorequal_params(args.xmp_in, args.xmp_out, params_gz)
    print(f"OK: patched colorequal params into {args.xmp_out}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
