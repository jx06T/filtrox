import streamlit as st
import re
import importlib
import io
from pathlib import Path
from PIL import Image

# 為了熱重載
import src.ai_engine, src.gmic_processor
importlib.reload(src.ai_engine)
importlib.reload(src.gmic_processor)

from src.ai_engine import AIEngine
from src.gmic_processor import GMICProcessor

# ================= 1. 配置 =================
st.set_page_config(page_title="AI G'MIC 修圖助手 v2", layout="wide")
BASE_DIR = Path(__file__).parent
GMIC_BIN = BASE_DIR / "gmic" / "gmic"
REF_FILE = BASE_DIR / "gmic_commands_edited.md"

# @st.cache_resource # 開發階段建議先不使用快取，或使用做法一的 version_tag
def init_engines():
    api_key = st.secrets["GEMINI_API_KEY"]
    ref_content = REF_FILE.read_text(encoding="utf-8") if REF_FILE.exists() else ""
    return AIEngine(api_key, ref_content), GMICProcessor(GMIC_BIN)

ai_engine, gmic_processor = init_engines()

# ================= 2. Session State =================
if 'history' not in st.session_state:
    st.session_state.history = [] 
if 'selected_idx' not in st.session_state:
    st.session_state.selected_idx = 0 
if 'last_uploaded_id' not in st.session_state:
    st.session_state.last_uploaded_id = None

# ================= 3. 輔助函式 =================
def add_to_history(img, cmd, mode):
    buf = io.BytesIO()
    img.save(buf, format="JPEG", quality=95)
    buf.seek(0)
    
    new_entry = {
        "img": img,
        "cmd": cmd,
        "type": mode, # "AI", "Manual", "Original"
        "buf": buf
    }
    # 放到隊伍最前面 (置頂)
    st.session_state.history.insert(0, new_entry)
    st.session_state.selected_idx = 0

# ================= 4. UI 介面 =================
st.title("🎨 AI 迭代修圖助手")

uploaded_file = st.sidebar.file_uploader("1. 上傳原始圖片", type=["jpg", "png", "jpeg"])

if uploaded_file:
    # --- 邏輯：偵測是否為新上傳的圖片 ---
    # 使用 name + size 作為簡單的 ID 辨識
    current_file_id = f"{uploaded_file.name}_{uploaded_file.size}"
    
    if st.session_state.last_uploaded_id != current_file_id:
        # 重置狀態並加入原圖
        st.session_state.history = []
        raw_img = Image.open(uploaded_file).convert("RGB")
        add_to_history(raw_img, "", "Original") # 原圖指令為空字串
        st.session_state.last_uploaded_id = current_file_id
        # 這裡不需要 rerun，因為下面會直接執行渲染
    
    # 始終從歷史紀錄的最底端拿取「原圖」作為處理基底
    # 因為我們是 insert(0)，所以最後一個永遠是原圖
    raw_img = st.session_state.history[-1]['img']
    
    col_main, col_hist = st.columns([1, 1])

    with col_main:
        # --- A. 編輯區 ---
        if st.session_state.history:
            current_item = st.session_state.history[st.session_state.selected_idx]
            
            # 計算版本編號 (顯示用)
            ver_num = len(st.session_state.history) - st.session_state.selected_idx
            st.subheader(f"🎯 當前編輯：版本 {ver_num}")
            
            st.image(current_item['img'], use_container_width=True)
            
            if current_item['type'] == "Original":
                st.info("這是原始圖片，尚未套用任何指令。")
            else:
                st.caption(f"目前套用指令: `{current_item['cmd']}`")
            
            base_cmd = current_item['cmd']

        # --- B. 輸入區 ---
        st.divider()
        user_text = st.text_input("🤖 AI 修改需求", placeholder="例如：讓圖片色彩變鮮豔、加強對比...")
        
        c1, c2 = st.columns(2)
        if c1.button("✨ AI 生成", type="primary", use_container_width=True):
            if user_text:
                with st.status("🚀 處理中...") as status:
                    status.write("🤖 AI 正在撰寫指令...")
                    new_cmd = ai_engine.get_gmic_command(user_text, base_cmd)
                    
                    status.write(f"🎨 G'MIC 執行中: `{new_cmd}`")
                    success, res_img, res_buf = gmic_processor.apply_effect(raw_img, new_cmd)
                    
                    if success:
                        add_to_history(res_img, new_cmd, "AI")
                        status.update(label="✅ 完成！", state="complete")
                        st.rerun()
                    else:
                        status.update(label="❌ 失敗", state="error")
                        st.error(res_img)

        with st.expander("🛠️ 手動輸入指令 (Debug)"):
            manual_cmd = st.text_input("G'MIC 指令", value=base_cmd)
            if st.button("執行手動指令", use_container_width=True):
                with st.status("🚀 處理中...") as status:
                    status.write(f"🎨 G'MIC 執行中")
                    success, res_img, res_buf = gmic_processor.apply_effect(raw_img, manual_cmd)
                    if success:
                        add_to_history(res_img, manual_cmd, "Manual")
                        status.update(label="✅ 完成！", state="complete")
                        st.rerun()
                    else:
                        status.update(label="❌ 失敗", state="error")
                        st.error(res_img)

    with col_hist:
        # --- C. 歷史紀錄區 ---
        st.subheader("📜 歷史紀錄 (最新在前)")
        
        for i, item in enumerate(st.session_state.history):
            # 選中的版本標記
            is_selected = (i == st.session_state.selected_idx)
            
            with st.container(border=True):
                hc1, hc2 = st.columns([1, 2])
                hc1.image(item['img'], use_container_width=True)
                
                # 標籤顯示
                if item['type'] == "Original":
                    label = "🖼️ 原始圖片"
                elif item['type'] == "AI":
                    label = "🤖 AI 生成"
                else:
                    label = "🛠️ 手動輸入"
                
                if is_selected:
                    hc2.markdown(f"**{label}** (編輯中)")
                else:
                    hc2.markdown(f"**{label}**")
                
                if item['cmd']:
                    hc2.code(item['cmd'], language="bash")
                else:
                    hc2.caption("無指令")
                
                # 功能按鈕
                btn_col1, btn_col2 = hc2.columns(2)
                if btn_col1.button("🎯 修改此版", key=f"mod_{i}"):
                    st.session_state.selected_idx = i
                    st.rerun()
                
                btn_col2.download_button(
                    label="📥 下載",
                    data=item['buf'],
                    file_name=f"ver_{len(st.session_state.history)-i}.jpg",
                    mime="image/jpeg",
                    key=f"dl_{i}"
                )

else:
    st.info("請先從左側邊欄上傳圖片以開始使用。")

# ================= CSS 優化 =================
st.markdown("""
<style>
    .stButton button { border-radius: 20px; }
    [data-testid="stExpander"] { border: none; background: #f0f2f6; border-radius: 10px; }
    /* 選中狀態的容器樣式 */
    .stColumn [data-testid="stVerticalBlock"] > div:has(button[kind="secondaryFormSubmit"]) {
        border-left: 5px solid red;
    }
</style>
""", unsafe_allow_html=True)