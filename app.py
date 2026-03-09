import streamlit as st
import os
import json
import uuid
import shutil
from typing import Optional, Dict, List
from datetime import datetime
from pathlib import Path
from PIL import Image, ImageDraw

# 引入您提供的組件
from src.photo_editing_agent import PhotoEditingAgent
from src.darktable_processor import DarktableProcessor
from src.llm_backend import Gemini
from dotenv import load_dotenv

load_dotenv()

# ================= 1. 配置與初始化 =================
API_KEY = os.getenv("GEMINI_API_KEY")
CLI_PATH = os.getenv("DARKTABLE_CLI_PATH", "darktable-cli")
GEMINI_MODEL = os.getenv("GEMINI_MODEL", "gemini-2.5-flash")
BASE_SAVE_DIR = Path("sessions") # 存放所有修圖紀錄的根目錄
SAVED_FILTERS_FILE = Path("saved_filters/filters.json")

@st.cache_resource
def init_engines():
    llm_service = Gemini(api_key=API_KEY,model_name=GEMINI_MODEL)
    agent = PhotoEditingAgent(llm_provider=llm_service)
    processor = DarktableProcessor(binary_path=CLI_PATH)
    return agent, processor

agent, processor = init_engines()

# ================= 2. Session State 初始化 =================
if "session_id" not in st.session_state:
    st.session_state.session_id = None      # 當前修圖資料夾名稱
    st.session_state.iteration = 0          # 第幾代
    st.session_state.current_variations = [] # 當前生成的組 (含路徑與參數)
    st.session_state.selected_params = None  # 使用者選中的上一代參數
    st.session_state.original_path = None    # 原始圖片路徑

    st.session_state.disliked_factors = {
        "exposure": [],
        "temperature": [],
        "tint": [],
        "vibrance": [],
        "saturation": [],
    }
    st.session_state.liked_factors = {
        "exposure": [],
        "temperature": [],
        "tint": [],
        "vibrance": [],
        "saturation": [],
    }
    # [修正] 新增狀態：暫存用戶當前代數選中的方案索引
    st.session_state.current_selected_idx_for_feedback = None 
    # [修正] 新增狀態：標記用戶是否已為當前代做出選擇
    st.session_state.has_made_selection_in_current_gen = False 

    st.session_state.selected_quick_feedback = []
    st.session_state.batch_output_dir = ""
    st.session_state.adhoc_session_id = None
    st.session_state.global_staged_files = []
    st.session_state.session_staged_files = []
    st.session_state.batch_studio_active = False
    st.session_state.batch_studio_staged_key = ""
    st.session_state.batch_studio_include_current = False
    st.session_state.batch_studio_session_id = ""
    st.session_state.batch_studio_output_dir = ""

# ================= 3. 輔助函式 =================

FACTOR_TOLERANCES = {
    "exposure": 0.05,
    "temperature": 50.0,
    "tint": 1.0,
    "vibrance": 3.0,
    "saturation": 1.0,
}

SUPPORTED_IMAGE_EXTS = {".jpg", ".jpeg", ".png", ".arw", ".cr2", ".nef", ".tif", ".tiff"}

def _extract_factors(variation_or_params: dict) -> Optional[Dict[str, float]]:
    """
    從一個變體字典 (e.g., {"params": {"factors": {...}}}) 或直接從 params 字典 (e.g., {"factors": {...}}) 中提取 factors。
    """
    factors_section = None

    # 情況A: 傳入的是 params 字典 (例如從 agent 直接回傳的數據)
    if "factors" in variation_or_params and isinstance(variation_or_params["factors"], dict):
        factors_section = variation_or_params["factors"]
    # 情況B: 傳入的是 session_state 中的 variation 字典 (包含 'params' key)
    elif "params" in variation_or_params and isinstance(variation_or_params["params"], dict):
        if "factors" in variation_or_params["params"] and isinstance(variation_or_params["params"]["factors"], dict):
            factors_section = variation_or_params["params"]["factors"]
    
    if not isinstance(factors_section, dict):
        return None

    extracted = {}
    for key in FACTOR_TOLERANCES:
        val = factors_section.get(key)
        if isinstance(val, (int, float)):
            extracted[key] = float(val)
    return extracted if extracted else None

def _is_disliked(factors: Dict[str, float], disliked: Dict[str, list]) -> bool:
    for key, val in factors.items():
        tol = FACTOR_TOLERANCES.get(key, 0.0)
        for blocked in disliked.get(key, []):
            if abs(val - blocked) <= tol:
                return True
    return False

def _filter_variations(variations: list, disliked: Dict[str, list]) -> list:
    filtered = []
    for var in variations:
        factors = _extract_factors(var)
        if factors and _is_disliked(factors, disliked):
            continue
        filtered.append(var)
    return filtered

def _apply_feedback_from_selection() -> None:
    """
    [修正] 核心邏輯修改：
    只有在點擊「產生下一代」時調用。
    比較「選中」與「未選中」的方案，只有當差異足夠大時，才將未選中的加入 disliked。
    """
    if st.session_state.current_selected_idx_for_feedback is None:
        return

    selected_idx = st.session_state.current_selected_idx_for_feedback
    variations = st.session_state.current_variations

    # 獲取被選中方案的關鍵因素
    selected_var = variations[selected_idx]
    selected_factors = _extract_factors(selected_var)
    
    if not selected_factors:
        # 重置狀態並返回
        st.session_state.current_selected_idx_for_feedback = None
        st.session_state.has_made_selection_in_current_gen = False
        return

    for idx, var in enumerate(variations):
        if idx == selected_idx:
            continue # 跳過選中的方案
        
        unselected_factors = _extract_factors(var)
        if not unselected_factors:
            continue

        # 遍歷未選中方案的每一個參數
        for key, unselected_val in unselected_factors.items():
            # 獲取選中方案的對應參數值
            selected_val = selected_factors.get(key)

            # 如果選中方案沒有這個參數，或者參數值差異顯著，才視為不喜歡
            if selected_val is None:
                # 這種情況較少見，但如果發生，可以認為是不喜歡的
                is_different = True
            else:
                # 使用容錯值來判斷差異是否「顯著」
                tol = FACTOR_TOLERANCES.get(key, 0.0)
                is_different = abs(unselected_val - selected_val) > tol

            if is_different:
                # 只有當參數值確實不同時，才將其加入不喜歡列表
                # 並且檢查是否已存在相似值
                if not any(abs(unselected_val - existing) <= FACTOR_TOLERANCES[key] for existing in st.session_state.disliked_factors[key]):
                    st.session_state.disliked_factors[key].append(unselected_val)
    
    # 2. 記錄喜歡的方案 (Liked)
    for key, val in selected_factors.items():
        if not any(abs(val - existing) <= FACTOR_TOLERANCES[key] for existing in st.session_state.liked_factors[key]):
            st.session_state.liked_factors[key].append(val)

    # 重置選擇狀態
    st.session_state.current_selected_idx_for_feedback = None
    st.session_state.has_made_selection_in_current_gen = False

def _compute_preferred_factors() -> Optional[Dict[str, float]]:
    preferred = {}
    for key, values in st.session_state.liked_factors.items():
        if values:
            preferred[key] = sum(values) / len(values)
    return preferred if preferred else None

def _variation_scale(iteration: int) -> float:
    # Reduce variation as iterations increase.
    return max(0.35, 1.0 - 0.15 * max(0, iteration - 1))

def _build_preview_image(image_path: str, is_selected: bool) -> Image.Image:
    """
    建立顯示用預覽圖。
    若為選中方案，直接在圖片內部繪製紅框，避免外擴邊框被 Streamlit 圓角/縮放裁切。
    """
    with Image.open(image_path) as img:
        preview = img.convert("RGB")

    if is_selected:
        draw = ImageDraw.Draw(preview)
        width, height = preview.size
        border_width = max(4, min(width, height) // 160)
        inset = border_width // 2 + 2
        radius = max(12, min(width, height) // 35)
        draw.rounded_rectangle(
            [inset, inset, width - inset - 1, height - inset - 1],
            radius=radius,
            outline=(255, 75, 75),
            width=border_width,
        )

    return preview

def _ensure_saved_filters_file() -> None:
    SAVED_FILTERS_FILE.parent.mkdir(parents=True, exist_ok=True)
    if not SAVED_FILTERS_FILE.exists():
        with open(SAVED_FILTERS_FILE, "w", encoding="utf-8") as f:
            json.dump([], f, ensure_ascii=False, indent=2)

def _load_saved_filters() -> List[dict]:
    _ensure_saved_filters_file()
    try:
        with open(SAVED_FILTERS_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
        if isinstance(data, list):
            return [x for x in data if isinstance(x, dict)]
    except Exception:
        pass
    return []

def _write_saved_filters(filters: List[dict]) -> None:
    _ensure_saved_filters_file()
    with open(SAVED_FILTERS_FILE, "w", encoding="utf-8") as f:
        json.dump(filters, f, ensure_ascii=False, indent=2)

def _save_filter(name: str, params: dict, preview_path: str) -> None:
    filters = _load_saved_filters()
    filters.append(
        {
            "id": uuid.uuid4().hex,
            "name": name.strip(),
            "params": params,
            "preview_path": preview_path,
            "created_at": datetime.now().isoformat(timespec="seconds"),
        }
    )
    _write_saved_filters(filters)

def _materialize_uploaded_files(uploaded_files, session_id: str) -> List[dict]:
    stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    source_root = Path(BASE_SAVE_DIR) / session_id / "batch_uploaded_source" / stamp
    source_root.mkdir(parents=True, exist_ok=True)
    materialized = []

    for idx, uploaded in enumerate(uploaded_files):
        original_name = Path(uploaded.name).name
        safe_name = f"{idx+1:04d}_{original_name}"
        target_path = source_root / safe_name
        with open(target_path, "wb") as f:
            f.write(uploaded.getbuffer())
        materialized.append(
            {
                "display_name": uploaded.name,
                "input_path": target_path.as_posix(),
            }
        )

    return materialized

def _file_display_name(file_item) -> str:
    if isinstance(file_item, dict):
        return str(file_item.get("display_name", "unknown"))
    return str(getattr(file_item, "name", "unknown"))

def _file_input_path(file_item) -> Optional[str]:
    if isinstance(file_item, dict):
        p = file_item.get("input_path")
        return str(p) if p else None
    return None

def _render_with_params(input_path: str, params: dict, output_path: str) -> Optional[str]:
    try:
        return processor.apply_effect(
            input_path=input_path,
            ai_params=params,
            output_path=output_path,
        )
    except Exception:
        return None

def _ensure_saved_filter_preview(saved_filter: dict, preview_input_path: str, session_id: str) -> Optional[str]:
    preview_root = Path(BASE_SAVE_DIR) / session_id / "saved_filter_previews"
    preview_root.mkdir(parents=True, exist_ok=True)
    in_stem = Path(preview_input_path).stem
    out_path = preview_root / f"{saved_filter['id']}_{in_stem}.jpg"
    if out_path.exists():
        return out_path.as_posix()
    out = _render_with_params(preview_input_path, saved_filter["params"], out_path.as_posix())
    return out

def _apply_assigned_filters(
    materialized_files: List[dict],
    output_folder: Path,
    filter_lookup: Dict[str, dict],
    assignments: Dict[int, str],
) -> Dict[str, object]:
    output_folder.mkdir(parents=True, exist_ok=True)
    used_names: Dict[str, int] = {}
    success = 0
    skipped = 0
    errors: List[str] = []
    total = len(materialized_files)
    progress = st.progress(0, text=f"開始批量處理（共 {total} 張）")

    for idx, item in enumerate(materialized_files, start=1):
        filter_key = assignments.get(idx - 1)
        filter_obj = filter_lookup.get(filter_key or "")
        if not filter_obj:
            skipped += 1
            progress.progress(idx / total, text=f"批量處理中：{idx}/{total}")
            continue

        base_name = Path(item["display_name"]).name
        stem = Path(base_name).stem
        default_suffix = Path(base_name).suffix or ".jpg"

        preview_path = item.get("preview_path")
        assigned_key = item.get("assigned_filter_key")
        if preview_path and assigned_key == filter_key and Path(preview_path).exists():
            out_suffix = Path(preview_path).suffix or ".jpg"
            name_seed = f"{stem}{out_suffix}"
            count = used_names.get(name_seed, 0)
            used_names[name_seed] = count + 1
            output_name = f"{stem}_{count:02d}{out_suffix}" if count > 0 else name_seed
            output_path = output_folder / output_name
            try:
                shutil.copy2(preview_path, output_path)
                success += 1
            except Exception:
                errors.append(f"{item['display_name']}: 複製暫存檔失敗")
        else:
            name_seed = f"{stem}{default_suffix}"
            count = used_names.get(name_seed, 0)
            used_names[name_seed] = count + 1
            output_name = f"{stem}_{count:02d}{default_suffix}" if count > 0 else name_seed
            output_path = (output_folder / output_name).as_posix()
            out = _render_with_params(item["input_path"], filter_obj["params"], output_path)
            if out:
                success += 1
            else:
                errors.append(f"{item['display_name']}: 渲染失敗")

        progress.progress(idx / total, text=f"批量處理中：{idx}/{total}")

    progress.empty()
    failed = len(errors)
    return {"success": success, "failed": failed, "skipped": skipped, "errors": errors}

def _get_effective_session_id() -> str:
    if st.session_state.session_id:
        return st.session_state.session_id
    if not st.session_state.adhoc_session_id:
        st.session_state.adhoc_session_id = f"adhoc_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
    return st.session_state.adhoc_session_id

def _build_filter_lookup(include_current_filters: bool) -> Dict[str, dict]:
    lookup: Dict[str, dict] = {}

    if include_current_filters:
        for i, var in enumerate(st.session_state.current_variations):
            key = f"current:{i}"
            lookup[key] = {
                "key": key,
                "label": f"[本次] 方案 {i+1}",
                "params": var["params"],
                "preview_path": var["path"],
                "source": "current",
                "index": i,
            }

    for sf in _load_saved_filters():
        key = f"saved:{sf['id']}"
        lookup[key] = {
            "key": key,
            "label": f"[已存] {sf.get('name', '未命名濾鏡')}",
            "params": sf.get("params", {}),
            "preview_path": sf.get("preview_path"),
            "source": "saved",
        }

    return lookup

def _apply_filter_to_selected(
    staged_key: str,
    selected_indices: List[int],
    filter_key: str,
    filter_lookup: Dict[str, dict],
    session_id: str,
) -> Dict[str, object]:
    staged_files = st.session_state.get(staged_key, [])
    filt = filter_lookup.get(filter_key)
    if not filt:
        return {"ok": 0, "errors": ["濾鏡不存在。"]}

    preview_root = Path(BASE_SAVE_DIR) / session_id / "batch_live_preview"
    preview_root.mkdir(parents=True, exist_ok=True)

    ok = 0
    errors: List[str] = []
    for idx in selected_indices:
        if idx < 0 or idx >= len(staged_files):
            continue
        item = staged_files[idx]
        stem = Path(item["display_name"]).stem
        version = int(item.get("_preview_version", 0)) + 1
        item["_preview_version"] = version
        out = preview_root / f"{idx:04d}_{stem}_{filter_key.replace(':', '_')}_v{version:03d}.jpg"
        rendered = _render_with_params(item["input_path"], filt["params"], out.as_posix())
        if rendered:
            item["preview_path"] = rendered
            item["assigned_filter_key"] = filter_key
            ok += 1
        else:
            errors.append(f"{item['display_name']}: 套用失敗")

    st.session_state[staged_key] = staged_files
    return {"ok": ok, "errors": errors}

def _studio_select_all_callback(staged_key: str) -> None:
    staged_files = st.session_state.get(staged_key, [])
    for i in range(len(staged_files)):
        st.session_state[f"{staged_key}_studio_pick_{i}"] = True

def _studio_deselect_all_callback(staged_key: str) -> None:
    staged_files = st.session_state.get(staged_key, [])
    for i in range(len(staged_files)):
        st.session_state[f"{staged_key}_studio_pick_{i}"] = False

def _studio_save_filter_callback(staged_key: str, filter_key: str, include_current: bool) -> None:
    filter_lookup = _build_filter_lookup(include_current)
    filt = filter_lookup.get(filter_key)
    if not filt:
        st.session_state.batch_studio_status_message = "濾鏡不存在。"
        return
    save_name_key = f"{staged_key}_save_name_{filter_key}"
    save_name = st.session_state.get(save_name_key, "").strip()
    if not save_name:
        st.session_state.batch_studio_status_message = "請先輸入濾鏡名稱。"
        return
    _save_filter(save_name, filt["params"], filt.get("preview_path", ""))
    st.session_state.batch_studio_status_message = f"已儲存濾鏡：{save_name}"

def _studio_apply_filter_callback(staged_key: str, filter_key: str, session_id: str, include_current: bool) -> None:
    staged_files = st.session_state.get(staged_key, [])
    selected_indices = [
        i for i in range(len(staged_files))
        if st.session_state.get(f"{staged_key}_studio_pick_{i}", False)
    ]
    if not selected_indices:
        st.session_state.batch_studio_status_message = "請先在左側勾選至少一張圖片。"
        return
    filter_lookup = _build_filter_lookup(include_current)
    result = _apply_filter_to_selected(
        staged_key,
        selected_indices,
        filter_key,
        filter_lookup,
        session_id,
    )
    if result["errors"]:
        st.session_state.batch_studio_status_message = (
            f"已套用 {result['ok']} 張；另有 {len(result['errors'])} 張失敗。"
        )
    else:
        st.session_state.batch_studio_status_message = f"已套用 {result['ok']} 張。"

def _studio_export_callback(staged_key: str, session_id: str, include_current: bool) -> None:
    staged_files = st.session_state.get(staged_key, [])
    filter_lookup = _build_filter_lookup(include_current)
    assignments = {
        i: item.get("assigned_filter_key")
        for i, item in enumerate(staged_files)
        if item.get("assigned_filter_key")
    }
    if st.session_state.batch_studio_output_dir.strip():
        output_folder = Path(st.session_state.batch_studio_output_dir.strip()).expanduser()
    else:
        output_folder = (
            Path(BASE_SAVE_DIR)
            / session_id
            / f"batch_assign_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        )
    result = _apply_assigned_filters(
        staged_files,
        output_folder,
        filter_lookup,
        assignments,
    )
    st.session_state.batch_studio_status_message = (
        f"完成：成功 {result['success']} 張，失敗 {result['failed']} 張，略過 {result['skipped']} 張。輸出：{output_folder.as_posix()}"
    )

def _render_batch_studio_left(staged_key: str, include_current: bool):
    staged_files = st.session_state.get(staged_key, [])
    filter_lookup = _build_filter_lookup(include_current)
    st.write("**圖片清單**")
    s1, s2 = st.columns(2)
    with s1:
        st.button(
            "全選",
            key=f"{staged_key}_studio_select_all",
            width="stretch",
            on_click=_studio_select_all_callback,
            args=(staged_key,),
        )
    with s2:
        st.button(
            "全不選",
            key=f"{staged_key}_studio_deselect_all",
            width="stretch",
            on_click=_studio_deselect_all_callback,
            args=(staged_key,),
        )

    grid = st.columns(3)
    for i, item in enumerate(staged_files):
        with grid[i % 3]:
            preview = item.get("preview_path") or item.get("input_path")
            if preview and Path(preview).exists():
                st.image(preview, width="stretch")
            st.checkbox(f"選取 #{i+1}", key=f"{staged_key}_studio_pick_{i}")
            assigned = item.get("assigned_filter_key")
            assigned_label = filter_lookup.get(assigned, {}).get("label", "(未分配)")
            st.caption(f"{_file_display_name(item)}\n{assigned_label}")

def _render_batch_studio_right(staged_key: str, session_id: str, include_current: bool):
    filter_lookup = _build_filter_lookup(include_current)
    st.write("**濾鏡列表**")
    st.text_input(
        "輸出資料夾路徑（可留空自動建立）",
        key="batch_studio_output_dir",
        placeholder="留空會建立在當前 session 目錄",
    )

    card_cols = st.columns(3)
    for idx, (key, filt) in enumerate(filter_lookup.items()):
        with card_cols[idx % 3]:
            st.markdown(f"**{filt['label']}**")
            p = filt.get("preview_path")
            if p and Path(p).exists():
                st.image(p, width="stretch")

            if filt.get("source") == "current":
                save_name_key = f"{staged_key}_save_name_{key}"
                if save_name_key not in st.session_state:
                    st.session_state[save_name_key] = f"gen{st.session_state.iteration}_v{filt.get('index', 0) + 1}"
                st.text_input("名稱", key=save_name_key)
                st.button(
                    "儲存濾鏡",
                    key=f"{staged_key}_save_btn_{key}",
                    width="stretch",
                    on_click=_studio_save_filter_callback,
                    args=(staged_key, key, include_current),
                )

            st.button(
                "套用此濾鏡",
                key=f"{staged_key}_apply_{key}",
                width="stretch",
                on_click=_studio_apply_filter_callback,
                args=(staged_key, key, session_id, include_current),
            )

    st.divider()
    st.button(
        "輸出全部已分配圖片",
        type="primary",
        width="stretch",
        on_click=_studio_export_callback,
        args=(staged_key, session_id, include_current),
    )

@st.fragment
def _render_batch_studio():
    staged_key = st.session_state.batch_studio_staged_key
    session_id = st.session_state.batch_studio_session_id or _get_effective_session_id()
    staged_files = st.session_state.get(staged_key, [])

    st.subheader("批量套用工作台")
    top_left, top_right = st.columns([1, 3])
    with top_left:
        if st.button("返回主畫面", width="stretch"):
            st.session_state.batch_studio_active = False
            st.rerun()
    with top_right:
        st.caption("左側勾選圖片，右側點濾鏡就會立刻套用並暫存預覽。")
    status_msg = st.session_state.get("batch_studio_status_message")
    if status_msg:
        st.info(status_msg)

    if not staged_files:
        st.warning("目前沒有批次圖片。")
        return

    filter_lookup = _build_filter_lookup(st.session_state.batch_studio_include_current)
    if not filter_lookup:
        st.warning("目前沒有可用濾鏡（請先生成或儲存濾鏡）。")
        return

    left, right = st.columns([3, 2])
    with left:
        _render_batch_studio_left(staged_key, st.session_state.batch_studio_include_current)
    with right:
        _render_batch_studio_right(staged_key, session_id, st.session_state.batch_studio_include_current)

def _render_group_assignment_ui(
    batch_files,
    filter_lookup: Dict[str, dict],
    state_prefix: str,
) -> Dict[int, str]:
    file_signature = tuple(_file_display_name(f) for f in batch_files)
    signature_key = f"{state_prefix}_file_signature"
    assign_key = f"{state_prefix}_assignments"

    if (
        signature_key not in st.session_state
        or st.session_state[signature_key] != file_signature
    ):
        st.session_state[signature_key] = file_signature
        st.session_state[assign_key] = {}
        st.session_state[f"{state_prefix}_selected_indices"] = []

    if assign_key not in st.session_state:
        st.session_state[assign_key] = {}

    assignments: Dict[int, str] = dict(st.session_state[assign_key])

    filter_keys = list(filter_lookup.keys())
    default_filter_key = filter_keys[0]
    selected_idx = st.session_state.get("current_selected_idx_for_feedback")
    if selected_idx is not None:
        preferred_key = f"current:{selected_idx}"
        if preferred_key in filter_lookup:
            default_filter_key = preferred_key

    st.write("**分配操作**")
    selected_indices_key = f"{state_prefix}_selected_indices"
    if selected_indices_key not in st.session_state:
        st.session_state[selected_indices_key] = []
    selected_set = set(st.session_state[selected_indices_key])

    ctrl1, ctrl2 = st.columns(2)
    with ctrl1:
        if st.button("全選目前批次", key=f"{state_prefix}_select_all_btn", width="stretch"):
            selected_set = set(range(len(batch_files)))
    with ctrl2:
        if st.button("取消全選", key=f"{state_prefix}_deselect_all_btn", width="stretch"):
            selected_set = set()

    st.caption("勾選你要套用同一個濾鏡的圖片（可複選）")
    grid_cols = st.columns(4)
    for i, file_item in enumerate(batch_files):
        col = grid_cols[i % 4]
        with col:
            img_path = _file_input_path(file_item)
            if img_path and Path(img_path).exists():
                st.image(img_path, width=170)
            st.caption(_file_display_name(file_item))
            checked = st.checkbox(
                f"選取 #{i+1}",
                value=(i in selected_set),
                key=f"{state_prefix}_pick_{i}",
            )
            if checked:
                selected_set.add(i)
            else:
                selected_set.discard(i)
    st.session_state[selected_indices_key] = sorted(selected_set)

    st.selectbox(
        "選擇要套用的濾鏡",
        options=filter_keys,
        format_func=lambda k: filter_lookup[k]["label"],
        key=f"{state_prefix}_selected_filter",
        index=filter_keys.index(default_filter_key),
    )

    c1, c2 = st.columns(2)
    with c1:
        if st.button("套用到這批圖片", key=f"{state_prefix}_assign_btn", width="stretch"):
            selected_indices = st.session_state.get(selected_indices_key, [])
            selected_filter = st.session_state.get(f"{state_prefix}_selected_filter", default_filter_key)
            if not selected_indices:
                st.warning("請先複選至少一張圖片。")
            else:
                for idx in selected_indices:
                    assignments[idx] = selected_filter
                st.session_state[assign_key] = assignments
                st.success(f"已分配 {len(selected_indices)} 張圖片。")
    with c2:
        if st.button("清空所有分配", key=f"{state_prefix}_clear_btn", width="stretch"):
            st.session_state[assign_key] = {}
            assignments = {}
            st.info("已清空。")

    st.write("**目前分配結果**")
    assigned_count = 0
    result_cols = st.columns(3)
    for i, f in enumerate(batch_files):
        k = assignments.get(i)
        col = result_cols[i % 3]
        with col:
            img_path = _file_input_path(f)
            if img_path and Path(img_path).exists():
                st.image(img_path, width=180)
            if k and k in filter_lookup:
                assigned_count += 1
                st.caption(f"{_file_display_name(f)} -> {filter_lookup[k]['label']}")
            else:
                st.caption(f"{_file_display_name(f)} -> (未分配)")
    st.caption(f"已分配 {assigned_count}/{len(batch_files)} 張")

    return assignments

def create_session_folder(original_name):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    folder_name = f"{Path(original_name).stem}_{timestamp}"
    path = BASE_SAVE_DIR / folder_name
    path.mkdir(parents=True, exist_ok=True)
    return path # 回傳 Path 物件



@st.cache_data
def get_session_history(session_id: str) -> Dict[int, List[str]]:
    """掃描 session 資料夾，回傳按代數整理好的圖片路徑字典"""
    if not session_id:
        return {}
        
    history = {}
    session_path = BASE_SAVE_DIR / session_id
    if not session_path.exists():
        return {}

    # 使用 glob 尋找符合模式的檔案
    # 檔名格式: {stem}_gen{代數}_v{版本}.jpg
    image_files = sorted(session_path.glob("*_gen*_v*.jpg"))
    
    for img_path in image_files:
        try:
            # 從檔名解析代數
            parts = img_path.stem.split('_')
            gen_part = [p for p in parts if p.startswith('gen')]
            if not gen_part:
                continue
            
            generation_num = int(gen_part[0].replace('gen', ''))
            
            if generation_num not in history:
                history[generation_num] = []
            history[generation_num].append(str(img_path))
        except (IndexError, ValueError):
            # 檔名格式不符，跳過
            continue
            
    # 按代數排序
    return dict(sorted(history.items()))


def run_generation(prompt=None, is_refinement=False, feedback=""):
    """執行 AI 生成與 Darktable 渲染的核心邏輯"""
    st.session_state.iteration += 1
    iter_idx = st.session_state.iteration
    
    with st.spinner(f"正在生成第 {iter_idx} 代修圖方案..."):
        # 1. 呼叫 AI 取得參數
        if not is_refinement:
            # 第一次冷啟動
            variations_data = agent.cold_start(prompt)
        else:
            # 迭代階段
            preferred_factors = _compute_preferred_factors()
            variation_scale = _variation_scale(iter_idx)
            if feedback.strip():
                # 有文字建議
                variations_data = agent.text_refine(
                    st.session_state.selected_params,
                    feedback,
                    st.session_state.disliked_factors,
                    preferred_factors,
                    variation_scale,
                )
            else:
                # 純點擊 (自動迭代)
                variations_data = agent.auto_iterate(
                    st.session_state.selected_params,
                    st.session_state.disliked_factors,
                    preferred_factors,
                    variation_scale,
                )

        if not variations_data:
            st.error("AI 生成參數失敗，請檢查 API 狀態。")
            return

        filtered_variations = _filter_variations(variations_data, st.session_state.disliked_factors)
        if not filtered_variations and variations_data:
            st.warning("自動過濾後沒有保留的可選方案，已回退到原始結果。")
            filtered_variations = variations_data
        
        # 2. 渲染圖片並儲存
        new_variations = []
        session_path = Path(BASE_SAVE_DIR) / st.session_state.session_id
        for i, var in enumerate(filtered_variations):
            # 檔名規範: {原圖名}_gen{第幾代}_{第幾張}.jpg
            stem = Path(st.session_state.original_path).stem
            file_name = f"{stem}_gen{iter_idx}_v{i+1}.jpg"

            output_img_path = (session_path / file_name).as_posix()
            input_img_path = Path(st.session_state.original_path).as_posix()
            
            try:
                # [維持外部調用] var 這裡是 parameters 字典
                processor.apply_effect(
                    input_path=input_img_path,
                    ai_params=var, 
                    output_path=output_img_path
                )
                output_xmp_path = Path(output_img_path).with_suffix(".xmp").as_posix()
                new_variations.append({
                    "name": f"方案 {i+1}", # 簡化 name 處理
                    "reasoning": "AI 生成", # 簡化 reasoning
                    "params": var,
                    "path": output_img_path,
                    "xmp_path": output_xmp_path,
                })
            except Exception as e:
                st.error(f"渲染失敗: {e}")

        st.session_state.current_variations = new_variations
        # 重置當前代的選擇狀態，確保新一代開始時沒有殘留選擇
        st.session_state.current_selected_idx_for_feedback = None
        st.session_state.has_made_selection_in_current_gen = False


# ================= 4. UI 介面 =================


@st.fragment
def render_history_fragment(session_id: str, current_iteration: int):
    """
    獨立渲染歷史紀錄的 Fragment。
    只有當 session_id 或 current_iteration 改變時，這裡才會重新渲染。
    這能保證在同一代內點擊按鈕時，歷史紀錄絕對不會閃爍。
    """
    history_data = get_session_history(session_id)
    if not history_data:
        st.caption("尚無歷史紀錄")
    else:
        for gen_num, img_paths in history_data.items():
            with st.expander(f"第 {gen_num} 代"):
                num_images = len(img_paths)
                image_width_unit = 2
                total_width_units = 10
                
                col_ratios = [image_width_unit] * num_images
                remaining_space = total_width_units - sum(col_ratios)
                
                if remaining_space > 0:
                    col_ratios.append(remaining_space)
                    
                cols = st.columns(col_ratios)
                
                for i, path in enumerate(img_paths):
                    if i < len(cols):
                        with cols[i]:
                            # 為了完美呈現燈箱效果，建議這裡加上 st.dialog (可選)
                            st.image(path, width=150)
                            # 如果您想加上點擊放大的按鈕，可以解除下面註解：
                            # if st.button("放大", key=f"view_hist_{path}", width="stretch"):
                            #    with st.dialog(f"第 {gen_num} 代 - 方案 {i+1}"):
                            #        st.image(path, width="stretch")



st.set_page_config(page_title="AI Darktable 迭代助手", layout="wide")
st.title("FiltroX 為使用者創造個人化相片濾鏡")

@st.dialog("直接批量套用（已儲存濾鏡）")
def global_saved_filters_batch_dialog():
    st.caption("這裡只會處理你剛剛在主畫面選好的那一批圖片。")
    batch_files = st.session_state.global_staged_files
    if batch_files:
        st.caption(f"目前批次：{len(batch_files)} 張")
    else:
        st.warning("目前沒有批次。請先在主畫面選圖並按「建立批次並開啟視窗」。")
        return

    st.text_input(
        "輸出資料夾路徑（可留空自動建立）",
        key="global_batch_output_dir",
        placeholder="留空會建立在 adhoc session 目錄",
    )

    saved_filters = _load_saved_filters()
    filter_lookup: Dict[str, dict] = {}
    for sf in saved_filters:
        sf_key = f"saved:{sf['id']}"
        filter_lookup[sf_key] = {
            "key": sf_key,
            "label": f"[已存] {sf.get('name', '未命名濾鏡')}",
            "params": sf.get("params", {}),
            "preview_path": sf.get("preview_path"),
        }

    page_options = ["已儲存濾鏡", "檔案分配"]
    if "global_batch_dialog_page" not in st.session_state:
        st.session_state.global_batch_dialog_page = "檔案分配"
    st.radio("頁面", options=page_options, key="global_batch_dialog_page", horizontal=True)

    effective_session_id = _get_effective_session_id()

    if st.session_state.global_batch_dialog_page == "已儲存濾鏡":
        if not saved_filters:
            st.caption("目前沒有已儲存濾鏡。")
        else:
            preview_input_path = None
            if batch_files:
                preview_input_path = batch_files[0]["input_path"]

            for sf in saved_filters:
                sf_key = f"saved:{sf['id']}"
                preview_path = sf.get("preview_path")
                if preview_input_path:
                    new_preview = _ensure_saved_filter_preview(sf, preview_input_path, effective_session_id)
                    if new_preview:
                        preview_path = new_preview
                        filter_lookup[sf_key]["preview_path"] = preview_path

                cols = st.columns([2, 3])
                with cols[0]:
                    if preview_path and Path(preview_path).exists():
                        st.image(preview_path, width=220)
                    else:
                        st.caption("尚無預覽圖")
                with cols[1]:
                    st.write(f"**{sf.get('name', '未命名濾鏡')}**")
                    st.caption(f"建立時間：{sf.get('created_at', '-')}")

    if st.session_state.global_batch_dialog_page == "檔案分配":
        st.divider()
        st.subheader("檔案分配")
        if not batch_files:
            st.info("請先選取要處理的圖片。")
            return
        if not filter_lookup:
            st.warning("目前沒有已儲存濾鏡可套用。")
            return

        assignments_map = _render_group_assignment_ui(
            batch_files,
            filter_lookup,
            state_prefix="global_batch",
        )

        if st.button("開始套用分配", type="primary", width="stretch"):
            materialized_files = batch_files
            assignments = {i: assignments_map.get(i) for i in range(len(batch_files))}
            unassigned = [i for i, v in assignments.items() if not v]
            if unassigned:
                st.warning(f"仍有 {len(unassigned)} 張圖片未分配濾鏡，請先完成分配。")
                return

            if st.session_state.global_batch_output_dir.strip():
                output_folder = Path(st.session_state.global_batch_output_dir.strip()).expanduser()
            else:
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                output_folder = (
                    Path(BASE_SAVE_DIR)
                    / effective_session_id
                    / f"batch_assign_{timestamp}"
                )

            with st.spinner("正在依照分配批量套用..."):
                result = _apply_assigned_filters(
                    materialized_files,
                    output_folder,
                    filter_lookup,
                    assignments,
                )
            st.success(
                f"批量完成：成功 {result['success']} 張，失敗 {result['failed']} 張。輸出：`{output_folder.as_posix()}`"
            )
            if result["errors"]:
                st.warning("部分檔案失敗：")
                for err in result["errors"][:12]:
                    st.code(err)

# --- 側邊欄：上傳與初始設定 ---
with st.sidebar:
    st.header("1. 上傳圖片")
    uploaded_file = st.file_uploader("選擇圖片 (JPG/RAW)", type=["jpg", "jpeg", "png", "arw", "cr2", "nef"])
    
    if uploaded_file:
        if st.session_state.original_path is None or uploaded_file.name not in st.session_state.original_path:
            folder = create_session_folder(uploaded_file.name)
            st.session_state.session_id = folder.name
            
            orig_save_path = (folder / f"original_{uploaded_file.name}").as_posix()
            with open(orig_save_path, "wb") as f:
                f.write(uploaded_file.getbuffer())
            
            st.session_state.original_path = orig_save_path
            
            # 重置所有狀態
            st.session_state.iteration = 0
            st.session_state.current_variations = []
            st.session_state.selected_params = None
            st.session_state.disliked_factors = {k: [] for k in FACTOR_TOLERANCES.keys()}
            st.session_state.liked_factors = {k: [] for k in FACTOR_TOLERANCES.keys()}
            st.session_state.current_selected_idx_for_feedback = None
            st.session_state.has_made_selection_in_current_gen = False
            st.rerun()

    st.divider()
    if st.session_state.original_path:
        st.image(st.session_state.original_path, caption="原始圖片", width="stretch")

    
    # --- 頁尾資訊 ---
    if st.session_state.session_id:
        with st.expander("檔案紀錄資訊"):
            st.write(f"當前工作資料夾: `sessions/{st.session_state.session_id}`")
            st.write(f"累計迭代次數: {st.session_state.iteration}")
            st.write("**不喜歡的參數紀錄 (Disliked):**")
            st.json(st.session_state.disliked_factors)
            st.write("**喜歡的參數紀錄 (Liked):**")
            st.json(st.session_state.liked_factors)
            

# --- 主畫面邏輯 ---
if st.session_state.batch_studio_active:
    _render_batch_studio()
    st.stop()

if not st.session_state.original_path:
    st.info("請先在左側上傳圖片。")
    st.markdown("### 直接批量套用（已儲存濾鏡）")
    global_pick_files = st.file_uploader(
        "先選一批要處理的圖片（可多選）",
        type=[ext.lstrip(".") for ext in SUPPORTED_IMAGE_EXTS],
        accept_multiple_files=True,
        key="global_batch_picker_files",
        width="stretch",
    )
    if global_pick_files:
        st.caption(f"已選擇 {len(global_pick_files)} 張，按下方按鈕進入分配視窗。")
    if st.button("建立批次並開啟視窗", width="stretch"):
        if not global_pick_files:
            st.warning("請先選取至少一張圖片。")
        else:
            effective_session_id = _get_effective_session_id()
            st.session_state.global_staged_files = _materialize_uploaded_files(
                global_pick_files,
                effective_session_id,
            )
            st.session_state["global_batch_selected_indices"] = []
            st.session_state.batch_studio_staged_key = "global_staged_files"
            st.session_state.batch_studio_include_current = False
            st.session_state.batch_studio_session_id = effective_session_id
            st.session_state.batch_studio_active = True
            st.rerun()
else:
    if st.session_state.session_id:
        render_history_fragment(st.session_state.session_id, st.session_state.iteration)
    else:
        st.caption("上傳圖片後將顯示歷史紀錄")

    
    # 第一階段：初始風格要求
    if st.session_state.iteration == 0:
        st.subheader("第一步：告訴 AI 你想要的風格")
        init_prompt = st.text_input("描述風格（例如：復古膠片感、賽博龐克、日系小清新）", key="init_prompt")
        if st.button("開始修圖"):
            if init_prompt:
                run_generation(prompt=init_prompt)
                get_session_history.clear() # 清理快取
                st.rerun() 
            else:
                st.warning("請輸入描述內容")
    
    @st.fragment
    def render_interactive_workspace():
        
        # --- 定義回呼函式 (Callbacks) ---
        # 這些函式會在按鈕被點擊後，且腳本重新執行"之前"被呼叫
        
        def select_variation_callback(idx, params):
            """處理選中方案的邏輯"""
            st.session_state.selected_params = params
            st.session_state.current_selected_idx_for_feedback = idx
            st.session_state.has_made_selection_in_current_gen = True

        def toggle_quick_feedback_callback(key):
            """處理快捷按鈕的切換邏輯"""
            if key in st.session_state.selected_quick_feedback:
                st.session_state.selected_quick_feedback.remove(key)
            else:
                st.session_state.selected_quick_feedback.append(key)
                
        # ----------------------------------------

        # 第二階段：迭代顯示區
        if st.session_state.iteration > 0 and st.session_state.current_variations:
            st.subheader(f"第 {st.session_state.iteration} 代生成結果")
            
            cols = st.columns(len(st.session_state.current_variations))
            
            for i, var in enumerate(st.session_state.current_variations):
                # 這裡讀取的狀態，保證是回呼函式執行過後的"最新"狀態
                is_selected = (st.session_state.current_selected_idx_for_feedback == i)
                
                with cols[i]:
                    preview_image = _build_preview_image(var["path"], is_selected)
                    st.image(preview_image, caption=f"方案 {i+1}", width="stretch")
                    
                    with st.expander("查看參數"):
                        st.json(var['params'])
                    
                    # 【關鍵修改】：使用 on_click 和 args 來綁定回呼函式
                    st.button(
                        f"{'已' if is_selected else ''}選中方案 {i+1}", 
                        key=f"btn_{i}",
                        on_click=select_variation_callback,
                        args=(i, var['params']) # 傳遞參數給回呼函式
                    )

            st.divider()

            # 迭代控制區
            if st.session_state.selected_params:
                st.subheader("繼續迭代")
                quick_feedback_options = {
                    "太暗": "Increase the exposure and lift the shadows.",
                    "太亮": "Reduce the exposure and lower the highlights.",
                    "太黃": "Make the color temperature cooler (more blue).",
                    "太藍": "Make the color temperature warmer (more yellow).",
                    "鮮豔點": "Increase the vibrance and saturation.",
                    "清淡點": "Decrease the vibrance and saturation.",
                }

                st.write("**快捷指令 (可多選):**")
                
                keys = list(quick_feedback_options.keys())
                row1_cols = st.columns(3)
                row2_cols = st.columns(3)
                
                for i, key in enumerate(keys):
                    col = row1_cols[i] if i < 3 else row2_cols[i - 3]
                    
                    with col:
                        # 這裡讀取的狀態也是最新的
                        is_selected = key in st.session_state.selected_quick_feedback
                        button_type = "primary" if is_selected else "secondary"
                        
                        # 【關鍵修改】：使用 on_click 綁定回呼函式
                        st.button(
                            key, 
                            width="stretch",
                            type=button_type,
                            on_click=toggle_quick_feedback_callback,
                            args=(key,) # 注意這裡傳遞單個參數時需要逗號
                        )

                feedback_col, button_col = st.columns([4, 1])

                with feedback_col:
                    feedback = st.text_input("或輸入更詳細的建議：", placeholder="例如：讓天空更藍...")

                with button_col:
                    st.write("") 
                    # 產生下一代按鈕的邏輯保持不變，因為它觸發的是全局的 run_generation
                    if st.button("產生下一代", type="primary", width="stretch"):
                        if st.session_state.has_made_selection_in_current_gen:
                            
                            quick_prompts = [quick_feedback_options[k] for k in st.session_state.selected_quick_feedback]
                            all_prompts = quick_prompts + [feedback.strip()]
                            final_feedback = ". ".join(p for p in all_prompts if p)
                            
                            if final_feedback:
                                st.info(f"正在傳送給 AI 的指令: {final_feedback}")
                            
                            _apply_feedback_from_selection()
                            run_generation(is_refinement=True, feedback=final_feedback)
                            
                            st.session_state.selected_quick_feedback.clear()
                            get_session_history.clear() 
                            st.rerun() # 這裡依然需要全局刷新
                        else:
                            st.warning("請先點擊上方圖片下的「選中方案」按鈕。")

                st.divider()
                @st.dialog("批量分配與濾鏡庫")
                def batch_assignment_dialog():
                    st.caption("在這裡你可以儲存濾鏡，並把不同濾鏡分配給不同圖片後一次套用。")
                    batch_files = st.session_state.session_staged_files
                    if batch_files:
                        st.caption(f"目前批次：{len(batch_files)} 張")
                    else:
                        st.warning("目前沒有批次。請先在主畫面選圖並按「建立批次」。")
                        return

                    st.text_input(
                        "輸出資料夾路徑（可留空自動建立）",
                        key="batch_output_dir",
                        placeholder="留空會建立在當前 session 目錄",
                    )

                    saved_filters = _load_saved_filters()
                    current_filters = []
                    filter_lookup: Dict[str, dict] = {}

                    for i, var in enumerate(st.session_state.current_variations):
                        key = f"current:{i}"
                        label = f"[本次] 方案 {i+1}"
                        filter_obj = {
                            "key": key,
                            "label": label,
                            "params": var["params"],
                            "preview_path": var["path"],
                        }
                        current_filters.append(filter_obj)
                        filter_lookup[key] = filter_obj

                    for sf in saved_filters:
                        sf_key = f"saved:{sf['id']}"
                        filter_lookup[sf_key] = {
                            "key": sf_key,
                            "label": f"[已存] {sf.get('name', '未命名濾鏡')}",
                            "params": sf.get("params", {}),
                            "preview_path": sf.get("preview_path"),
                        }

                    page_options = ["本次生成濾鏡", "已儲存濾鏡", "檔案分配"]
                    if "batch_dialog_page" not in st.session_state:
                        st.session_state.batch_dialog_page = "本次生成濾鏡"
                    st.radio(
                        "頁面",
                        options=page_options,
                        key="batch_dialog_page",
                        horizontal=True,
                    )

                    if st.session_state.batch_dialog_page == "本次生成濾鏡":
                        if not current_filters:
                            st.caption("目前沒有可用的本次濾鏡。")
                        else:
                            for i, filt in enumerate(current_filters):
                                row = st.columns([2, 3])
                                with row[0]:
                                    st.image(filt["preview_path"], width=220)
                                with row[1]:
                                    st.write(f"**{filt['label']}**")
                                    name_key = f"save_filter_name_{st.session_state.session_id}_{st.session_state.iteration}_{i}"
                                    if name_key not in st.session_state:
                                        st.session_state[name_key] = f"gen{st.session_state.iteration}_v{i+1}"
                                    st.text_input("濾鏡名稱", key=name_key)
                                    if st.button("儲存此濾鏡", key=f"save_filter_btn_{i}", width="stretch"):
                                        filter_name = st.session_state.get(name_key, "").strip()
                                        if not filter_name:
                                            st.warning("請先輸入濾鏡名稱。")
                                        else:
                                            _save_filter(filter_name, filt["params"], filt["preview_path"])
                                            st.success(f"已儲存濾鏡：{filter_name}")

                    if st.session_state.batch_dialog_page == "已儲存濾鏡":
                        if not saved_filters:
                            st.caption("目前沒有已儲存濾鏡。")
                        else:
                            preview_input_path = None
                            if batch_files:
                                preview_input_path = batch_files[0]["input_path"]

                            for sf in saved_filters:
                                sf_key = f"saved:{sf['id']}"
                                preview_path = sf.get("preview_path")
                                if preview_input_path:
                                    new_preview = _ensure_saved_filter_preview(sf, preview_input_path, st.session_state.session_id)
                                    if new_preview:
                                        preview_path = new_preview
                                if sf_key in filter_lookup:
                                    filter_lookup[sf_key]["preview_path"] = preview_path

                                block = st.columns([2, 3])
                                with block[0]:
                                    if preview_path and Path(preview_path).exists():
                                        st.image(preview_path, width=220)
                                    else:
                                        st.caption("尚無預覽圖")
                                with block[1]:
                                    st.write(f"**{sf.get('name', '未命名濾鏡')}**")
                                    st.caption(f"建立時間：{sf.get('created_at', '-')}")

                    if st.session_state.batch_dialog_page == "檔案分配":
                        st.divider()
                        st.subheader("檔案分配")
                        if not batch_files:
                            st.info("請先選取要處理的圖片。")
                            return
                        if not filter_lookup:
                            st.warning("目前沒有可用濾鏡。")
                            return

                        assignments_map = _render_group_assignment_ui(
                            batch_files,
                            filter_lookup,
                            state_prefix=f"session_batch_{st.session_state.session_id}",
                        )

                        if st.button("開始套用分配", type="primary", width="stretch"):
                            materialized_files = batch_files
                            assignments = {i: assignments_map.get(i) for i in range(len(batch_files))}
                            unassigned = [i for i, v in assignments.items() if not v]
                            if unassigned:
                                st.warning(f"仍有 {len(unassigned)} 張圖片未分配濾鏡，請先完成分配。")
                                return

                            if st.session_state.batch_output_dir.strip():
                                output_folder = Path(st.session_state.batch_output_dir.strip()).expanduser()
                            else:
                                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                                output_folder = (
                                    Path(BASE_SAVE_DIR)
                                    / st.session_state.session_id
                                    / f"batch_assign_{timestamp}"
                                )

                            with st.spinner("正在依照分配批量套用..."):
                                result = _apply_assigned_filters(
                                    materialized_files,
                                    output_folder,
                                    filter_lookup,
                                    assignments,
                                )
                            st.success(
                                f"批量完成：成功 {result['success']} 張，失敗 {result['failed']} 張。輸出：`{output_folder.as_posix()}`"
                            )
                            if result["errors"]:
                                st.warning("部分檔案失敗：")
                                for err in result["errors"][:12]:
                                    st.code(err)

                st.markdown("### 批次圖片")
                session_pick_files = st.file_uploader(
                    "先選一批要處理的圖片（可多選）",
                    type=[ext.lstrip(".") for ext in SUPPORTED_IMAGE_EXTS],
                    accept_multiple_files=True,
                    key="session_batch_picker_files",
                    width="stretch",
                )
                if session_pick_files:
                    st.caption(f"已選擇 {len(session_pick_files)} 張，請先按「建立批次」。")

                if st.button("建立批次", width="stretch"):
                    if not session_pick_files:
                        st.warning("請先選取至少一張圖片。")
                    else:
                        st.session_state.session_staged_files = _materialize_uploaded_files(
                            session_pick_files,
                            st.session_state.session_id,
                        )
                        st.session_state[f"session_batch_{st.session_state.session_id}_selected_indices"] = []
                        st.success(f"已建立批次，共 {len(st.session_state.session_staged_files)} 張。")

                open_col1, open_col2 = st.columns(2)
                with open_col1:
                    if st.button("開啟濾鏡視窗", width="stretch"):
                        if not st.session_state.session_staged_files:
                            st.warning("請先建立批次。")
                        else:
                            st.session_state.batch_studio_staged_key = "session_staged_files"
                            st.session_state.batch_studio_include_current = True
                            st.session_state.batch_studio_session_id = st.session_state.session_id
                            st.session_state.batch_studio_active = True
                            st.rerun()
                with open_col2:
                    if st.button("直接批量套用", width="stretch"):
                        if not st.session_state.session_staged_files:
                            st.warning("請先建立批次。")
                        else:
                            st.session_state.batch_studio_staged_key = "session_staged_files"
                            st.session_state.batch_studio_include_current = True
                            st.session_state.batch_studio_session_id = st.session_state.session_id
                            st.session_state.batch_studio_active = True
                            st.rerun()

    # 4. 呼叫這個工作區 Fragment
    render_interactive_workspace()
