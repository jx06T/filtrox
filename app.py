import streamlit as st
import os
import time
import json
from typing import Optional, Dict, List
from datetime import datetime
from pathlib import Path
from PIL import Image

# 引入您提供的組件
from src.photo_editing_agent import PhotoEditingAgent
from src.darktable_processor import DarktableProcessor
from src.llm_backend import Gemini
from dotenv import load_dotenv

load_dotenv()

# ================= 1. 配置與初始化 =================
API_KEY = os.getenv("GEMINI_API_KEY")
CLI_PATH = "darktable-cli"  # 確保 darktable-cli 在 PATH 中
BASE_SAVE_DIR = Path("sessions") # 存放所有修圖紀錄的根目錄

# @st.cache_resource
def init_engines():
    llm_service = Gemini(api_key=API_KEY)
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

# ================= 3. 輔助函式 =================

FACTOR_TOLERANCES = {
    "exposure": 0.05,
    "temperature": 50.0,
    "tint": 1.0,
    "vibrance": 3.0,
    "saturation": 1.0,
}

def _extract_factors(config: dict) -> Optional[Dict[str, float]]:
    factors = config.get("factors")
    if not isinstance(factors, dict):
        return None
    extracted = {}
    for key in FACTOR_TOLERANCES:
        val = factors.get(key)
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

def _remember_disliked_from_unselected(selected_idx: int, variations: list) -> None:
    for idx, var in enumerate(variations):
        if idx == selected_idx:
            continue
        factors = _extract_factors(var.get("params", {}))
        if not factors:
            continue
        for key, val in factors.items():
            if not any(abs(val - existing) <= FACTOR_TOLERANCES[key] for existing in st.session_state.disliked_factors[key]):
                st.session_state.disliked_factors[key].append(val)

def _remember_liked_from_selected(selected: dict) -> None:
    factors = _extract_factors(selected.get("params", {}))
    if not factors:
        return
    for key, val in factors.items():
        st.session_state.liked_factors[key].append(val)

def _compute_preferred_factors() -> Optional[Dict[str, float]]:
    preferred = {}
    for key, values in st.session_state.liked_factors.items():
        if values:
            preferred[key] = sum(values) / len(values)
    return preferred if preferred else None

def _variation_scale(iteration: int) -> float:
    # Reduce variation as iterations increase.
    return max(0.35, 1.0 - 0.15 * max(0, iteration - 1))

def create_session_folder(original_name):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    folder_name = f"{Path(original_name).stem}_{timestamp}"
    path = BASE_SAVE_DIR / folder_name
    path.mkdir(parents=True, exist_ok=True)
    return path # 回傳 Path 物件

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
        print(filtered_variations)
        
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
                processor.apply_effect(
                    input_path=input_img_path,
                    ai_params=var,
                    output_path=output_img_path
                )
                new_variations.append({
                    "name": "name",
                    "reasoning": "reasoning",
                    "params": var,
                    "path": output_img_path
                })
            except Exception as e:
                st.error(f"渲染失敗: {e}")

        st.session_state.current_variations = new_variations

# ================= 4. UI 介面 =================

st.set_page_config(page_title="AI Darktable 迭代助手", layout="wide")
st.title("🎨 AI Darktable 迭代修圖助手")

# --- 側邊欄：上傳與初始設定 ---
with st.sidebar:
    st.header("1. 上傳圖片")
    uploaded_file = st.file_uploader("選擇圖片 (JPG/RAW)", type=["jpg", "jpeg", "png", "arw", "cr2", "nef"])
    
    if uploaded_file:
        if st.session_state.original_path is None or uploaded_file.name not in st.session_state.original_path:
            folder = create_session_folder(uploaded_file.name)
            st.session_state.session_id = folder.name
            
            # 使用 .as_posix()
            orig_save_path = (folder / f"original_{uploaded_file.name}").as_posix()
            with open(orig_save_path, "wb") as f:
                f.write(uploaded_file.getbuffer())
            
            st.session_state.original_path = orig_save_path

    st.divider()
    if st.session_state.original_path:
        st.image(st.session_state.original_path, caption="原始圖片", use_container_width=True)

# --- 主畫面邏輯 ---
if not st.session_state.original_path:
    st.info("請先在左側上傳圖片。")
else:
    # 第一階段：初始風格要求
    if st.session_state.iteration == 0:
        st.subheader("🚀 第一步：告訴 AI 你想要的風格")
        init_prompt = st.text_input("描述風格（例如：復古膠片感、賽博龐克、日系小清新）", key="init_prompt")
        if st.button("開始修圖"):
            if init_prompt:
                run_generation(prompt=init_prompt)
                st.rerun()
            else:
                st.warning("請輸入描述內容")
    
    # 第二階段：迭代顯示區
    if st.session_state.iteration > 0 and st.session_state.current_variations:
        st.subheader(f"✨ 第 {st.session_state.iteration} 代生成結果")
        
        cols = st.columns(len(st.session_state.current_variations))
        
        for i, var in enumerate(st.session_state.current_variations):
            with cols[i]:
                st.image(var['path'], caption=f"方案 {i+1}: {var['name']}", use_container_width=True)
                with st.expander("查看 AI 理由與參數"):
                    st.write(f"**理由:** {var['reasoning']}")
                    st.json(var['params'])
                
                # 選擇按鈕
                if st.button(f"🎯 選中方案 {i+1}", key=f"btn_{i}"):
                    _remember_disliked_from_unselected(i, st.session_state.current_variations)
                    _remember_liked_from_selected(var)
                    st.session_state.selected_params = var['params']
                    st.toast(f"已選中方案 {i+1}")

        st.divider()

        # 迭代控制區
        if st.session_state.selected_params:
            st.subheader("🔄 繼續迭代")
            col_fb, col_go = st.columns([4, 1])
            feedback = col_fb.text_input("輸入修改建議 (若留白則由 AI 自動優化)", placeholder="例如：再亮一點、陰影藍一點...")
            
            if col_go.button("產生下一代", type="primary"):
                run_generation(is_refinement=True, feedback=feedback)
                st.rerun()

# --- 頁尾資訊 ---
if st.session_state.session_id:
    with st.expander("📁 檔案紀錄資訊"):
        st.write(f"當前工作資料夾: `sessions/{st.session_state.session_id}`")
        st.write(f"累計迭代次數: {st.session_state.iteration}")
