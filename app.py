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

@st.cache_resource
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
    # [修正] 新增狀態：暫存用戶當前代數選中的方案索引
    st.session_state.current_selected_idx_for_feedback = None 
    # [修正] 新增狀態：標記用戶是否已為當前代做出選擇
    st.session_state.has_made_selection_in_current_gen = False 

    st.session_state.selected_quick_feedback = []

# ================= 3. 輔助函式 =================

FACTOR_TOLERANCES = {
    "exposure": 0.05,
    "temperature": 50.0,
    "tint": 1.0,
    "vibrance": 3.0,
    "saturation": 1.0,
}

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
                new_variations.append({
                    "name": f"方案 {i+1}", # 簡化 name 處理
                    "reasoning": "AI 生成", # 簡化 reasoning
                    "params": var,
                    "path": output_img_path
                })
            except Exception as e:
                st.error(f"渲染失敗: {e}")

        st.session_state.current_variations = new_variations
        # 重置當前代的選擇狀態，確保新一代開始時沒有殘留選擇
        st.session_state.current_selected_idx_for_feedback = None
        st.session_state.has_made_selection_in_current_gen = False


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
        st.image(st.session_state.original_path, caption="原始圖片", use_container_width=True)

    
    # --- 頁尾資訊 ---
    if st.session_state.session_id:
        with st.expander("📁 檔案紀錄資訊"):
            st.write(f"當前工作資料夾: `sessions/{st.session_state.session_id}`")
            st.write(f"累計迭代次數: {st.session_state.iteration}")
            st.write("**不喜歡的參數紀錄 (Disliked):**")
            st.json(st.session_state.disliked_factors)
            st.write("**喜歡的參數紀錄 (Liked):**")
            st.json(st.session_state.liked_factors)
            

# --- 主畫面邏輯 ---
if not st.session_state.original_path:
    st.info("請先在左側上傳圖片。")
else:
    if st.session_state.session_id:
        history_data = get_session_history(st.session_state.session_id)
        if not history_data:
            st.caption("尚無歷史紀錄")
        else:
            # for gen_num, img_paths in reversed(history_data.items()):
            for gen_num, img_paths in history_data.items():
                with st.expander(f"第 {gen_num} 代"):
                    num_images = len(img_paths)
                
                    image_width_unit = 2
                    total_width_units = 10
                    
                    col_ratios = [image_width_unit] * num_images
                    remaining_space = total_width_units - sum(col_ratios)
                    
                    # 如果有剩餘空間，就添加一個空白欄
                    if remaining_space > 0:
                        col_ratios.append(remaining_space)
                        
                    cols = st.columns(col_ratios)
                    
                    for i, path in enumerate(img_paths):
                        # 確保我們只在圖片欄裡放圖片
                        if i < len(cols):
                            with cols[i]:
                                st.image(path, use_container_width=True, width=150)
                                # 也可以加上標題
                                # st.caption(Path(path).name)
    else:
        st.caption("上傳圖片後將顯示歷史紀錄")

    
    # 第一階段：初始風格要求
    if st.session_state.iteration == 0:
        st.subheader("🚀 第一步：告訴 AI 你想要的風格")
        init_prompt = st.text_input("描述風格（例如：復古膠片感、賽博龐克、日系小清新）", key="init_prompt")
        if st.button("開始修圖"):
            if init_prompt:
                run_generation(prompt=init_prompt)
                get_session_history.clear() # 清理快取
                st.rerun() 
            else:
                st.warning("請輸入描述內容")
    
    # 第二階段：迭代顯示區
    if st.session_state.iteration > 0 and st.session_state.current_variations:
        st.subheader(f"✨ 第 {st.session_state.iteration} 代生成結果")
        
        cols = st.columns(len(st.session_state.current_variations))
        
        for i, var in enumerate(st.session_state.current_variations):
            # [修正] 視覺反饋：檢查該方案是否為「當前暫時選中」
            is_selected = (st.session_state.current_selected_idx_for_feedback == i)
            
            with cols[i]:
                # 使用 HTML/CSS 增加選中邊框
                border_style = "3px solid #FF4B4B" if is_selected else "1px solid #ddd"
                st.markdown(
                    f'<div style="border: {border_style}; padding: 5px; border-radius: 5px;">', 
                    unsafe_allow_html=True
                )
                st.image(var['path'], caption=f"方案 {i+1}", use_container_width=True)
                st.markdown('</div>', unsafe_allow_html=True)
                
                with st.expander("查看參數"):
                    st.json(var['params'])
                
                # [修正] 選中按鈕邏輯
                # 點擊只更新暫存狀態，不立即寫入 disliked/liked
                if st.button(f"🎯 {'已' if st.session_state.current_selected_idx_for_feedback == i else ''}選中方案 {i+1}", key=f"btn_{i}"):
                    st.session_state.selected_params = var['params']
                    st.session_state.current_selected_idx_for_feedback = i
                    st.session_state.has_made_selection_in_current_gen = True
                    st.rerun() # 刷新以顯示邊框

        st.divider()

        # 迭代控制區
        # 只要前一代有被選中的參數 (意味著已經進入了迭代循環)，就顯示介面
        # 但按鈕的有效性取決於當前代是否做出了選擇
        if st.session_state.selected_params:
            st.subheader("🔄 繼續迭代")

            quick_feedback_options = {
                "太暗": "Increase the exposure and lift the shadows.",
                "太亮": "Reduce the exposure and lower the highlights.",
                "太黃": "Make the color temperature cooler (more blue).",
                "太藍": "Make the color temperature warmer (more yellow).",
                "鮮豔點": "Increase the vibrance and saturation.",
                "清淡點": "Decrease the vibrance and saturation.",
            }

            # --- 快捷按鈕 UI 與邏輯 (支援多選和高亮) ---
            st.write("**快捷指令 (可多選):**")
            
            keys = list(quick_feedback_options.keys())
            # 建立一個持久的列容器，避免在循環中重複創建
            row1_cols = st.columns(3)
            row2_cols = st.columns(3)
            
            for i, key in enumerate(keys):
                # 根據索引分配到對應的行和列
                col = row1_cols[i] if i < 3 else row2_cols[i - 3]
                
                with col:
                    is_selected = key in st.session_state.selected_quick_feedback
                    button_type = "primary" if is_selected else "secondary"
                    
                    if st.button(key, use_container_width=True, type=button_type):
                        if is_selected:
                            st.session_state.selected_quick_feedback.remove(key)
                        else:
                            st.session_state.selected_quick_feedback.append(key)
                        st.rerun()

            # --- 文字輸入與生成按鈕 ---
            # 使用新的佈局來放置輸入框和按鈕
            feedback_col, button_col = st.columns([4, 1])

            with feedback_col:
                feedback = st.text_input("或輸入更詳細的建議：", placeholder="例如：讓天空更藍...")

            with button_col:
                # 為了對齊，我們可以使用一個空元素或調整垂直對齊，但簡單的 st.button 通常也夠用
                st.write("") # 佔位符，讓按鈕和輸入框頂部大致對齊
                if st.button("產生下一代", type="primary", use_container_width=True):
                    if st.session_state.has_made_selection_in_current_gen:
                        
                        # 組合所有反饋
                        quick_prompts = [quick_feedback_options[key] for key in st.session_state.selected_quick_feedback]
                        all_prompts = quick_prompts + [feedback.strip()]
                        final_feedback = ". ".join(p for p in all_prompts if p)
                        
                        # 顯示即將發送的指令
                        if final_feedback:
                            st.info(f"🤖 **正在傳送給 AI 的指令:** {final_feedback}")
                        
                        # 執行生成
                        _apply_feedback_from_selection()
                        run_generation(is_refinement=True, feedback=final_feedback) # 注意：run_generation 內部不應該有 st.rerun()

                        # 清理狀態並觸發刷新
                        st.session_state.selected_quick_feedback.clear()
                        get_session_history.clear() # 清除歷史快取
                        st.rerun() # 在所有操作完成後，統一在這裡刷新
                    else:
                        st.warning("請先點擊上方圖片下的「🎯 選中方案」按鈕。")


