import base64
import ctypes
import re
import zlib
from ctypes import c_float, c_int32
from typing import Any, Dict, Optional, Tuple

# =========================
# 1. 基礎設定與編碼工具
# =========================
HEX_OPS = {"exposure", "sigmoid", "toneequal"}
CHANNEL_SIZE = 4

def _dt_encode_gz(raw: bytes, level: int = 9) -> str:
    """Darktable 特有的 gz 編碼格式"""
    comp = zlib.compress(raw, level=level)
    clen = len(comp)
    if clen == 0:
        raise ValueError("zlib produced empty output")
    factor = min((len(raw) // clen) + 1, 99)
    return f"gz{factor:02d}" + base64.b64encode(comp).decode("ascii")

def _encode_params(op: str, raw: bytes, force_format: Optional[str] = None) -> str:
    """決定使用 Hex 還是 GZ 編碼"""
    if force_format == "hex":
        return raw.hex()
    if force_format == "gz":
        return _dt_encode_gz(raw)
    if op in HEX_OPS:
        return raw.hex()
    return _dt_encode_gz(raw)

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


# =========================
# 3. XML 處理邏輯
# =========================
def _find_rdf_li_start_tag(doc: str, operation: str) -> Optional[Tuple[int, int, str]]:
    op = re.escape(operation)
    pat = re.compile(rf'(<rdf:li\b[^>]*\bdarktable:operation=(["\']){op}\2[^>]*>)', flags=re.DOTALL)
    m = pat.search(doc)
    return (m.start(1), m.end(1), m.group(1)) if m else None

def _replace_or_insert_attr(tag: str, attr: str, value: str) -> str:
    pat = re.compile(rf'(\s{re.escape(attr)}=)(["\'])(.*?)(\2)', flags=re.DOTALL)
    if pat.search(tag):
        return pat.sub(lambda m: m.group(1) + m.group(2) + value + m.group(4), tag, count=1)
    if tag.endswith("/>"): return tag[:-2] + f' {attr}="{value}"' + "/>"
    if tag.endswith(">"): return tag[:-1] + f' {attr}="{value}"' + ">"
    return tag

def _fill_struct(st: ctypes.Structure, params: Dict[str, Any]) -> None:
    if isinstance(st, ColorBalanceRGBParams):
        st.saturation_global = 1.0  # 預設飽和度為 1 (正常)
        st.saturation_formula = 1   # 預設使用新的飽和度公式
        st.grey_fulcrum = 0.18      # 標準灰點
        st.contrast = 0.0           # 預設對比不變
        # 其他 Y, C, H 預設為 0.0

    for field_name, field_type in getattr(st, "_fields_", []):
        if field_name not in params: continue
        v = params[field_name]
        try:
            cur = getattr(st, field_name)
            if isinstance(cur, ctypes.Array): # Handle arrays like in ChannelMixer
                if isinstance(v, list):
                    for i in range(min(len(cur), len(v))): cur[i] = float(v[i])
            else:
                setattr(st, field_name, float(v) if field_type is c_float else int(v))
        except Exception: continue

# =========================
# 4. 主類別：XMPPatcher
# =========================
class XMPPatcher:
    """負責將 Dict 參數注入 XMP 字串的工具類"""

    @staticmethod
    def patch_xmp_content(xmp_content: str, modules_config: Dict[str, Any]) -> str:
        """
        核心方法：接收原始 XMP 內容與模組設定，回傳修改後的 XMP 內容
        :param xmp_content: 原始 XMP 字串
        :param modules_config: 包含模組設定的 Dict, 例如: {'colorbalancergb': {'params': {...}}}
        :return: 修改後的 XMP 字串
        """
        doc = xmp_content
        
        # 支援直接傳入單層 config，也支援包在 'modules' key 底下
        if "modules" in modules_config:
            modules_config = modules_config["modules"]

        for op, mcfg in modules_config.items():
            if not isinstance(mcfg, dict): continue

            # 1. 計算參數 Blob
            params_str = None
            st_cls = OP_TO_STRUCT.get(op)
            
            if st_cls and "params" in mcfg:
                st = st_cls()
                _fill_struct(st, mcfg["params"])
                raw = bytes(st)
                params_str = _encode_params(op, raw)

            # 2. 修改 XML 標籤
            found = _find_rdf_li_start_tag(doc, op)
            if found:
                s, e, tag = found
                new_tag = tag
                
                # 處理啟用狀態 (enabled)
                if "enabled" in mcfg:
                    new_tag = _replace_or_insert_attr(new_tag, "darktable:enabled", str(int(mcfg["enabled"])))
                
                # 處理參數字串 (params)
                if params_str:
                    new_tag = _replace_or_insert_attr(new_tag, "darktable:params", params_str)

                # 替換字串
                doc = doc[:s] + new_tag + doc[e:]

        return doc