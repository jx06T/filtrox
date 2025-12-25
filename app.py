import streamlit as st
import re
from pathlib import Path
from PIL import Image

import importlib
import src.ai_engine
import src.gmic_processor

# 強制重新載入
importlib.reload(src.ai_engine)
importlib.reload(src.gmic_processor)

from src.ai_engine import AIEngine
from src.gmic_processor import GMICProcessor

# ================= 配置與初始化 =================
st.set_page_config(page_title="AI G'MIC 修圖助手", layout="wide")

# 常數設定
BASE_DIR = Path(__file__).parent
GMIC_BIN = BASE_DIR / "gmic" / "gmic"
REF_FILE = BASE_DIR / "gmic_commands_edited.md"

# @st.cache_data
def load_reference():
    return REF_FILE.read_text(encoding="utf-8") if REF_FILE.exists() else "No reference data."

# @st.cache_resource
def init_engines():
    try:
        api_key = st.secrets["GEMINI_API_KEY"]
        ref_content = load_reference()
        ai = AIEngine(api_key, ref_content)
        proc = GMICProcessor(GMIC_BIN)
        return ai, proc
    except Exception as e:
        st.error(f"初始化失敗: {e}")
        st.stop()

ai_engine, gmic_processor = init_engines()

# ================= Session State =================
if 'processed_image' not in st.session_state:
    st.session_state.update({
        'processed_image': None,
        'current_cmd': None,
        'download_buffer': None
    })

# ================= UI 介面 =================
st.title("AI 自然語言修圖助手 (G'MIC 版)")

col1, col2 = st.columns([1, 1.5])

with col1:
    uploaded_file = st.file_uploader("上傳一張圖片", type=["jpg", "png", "jpeg"])
    
    if uploaded_file:
        raw_img = Image.open(uploaded_file).convert("RGB")
        st.image(raw_img, caption="原始圖片", use_container_width=True)
        
        st.divider()
        st.subheader("🤖 AI 自動生成")
        user_text = st.text_area("描述您想要的修圖效果", placeholder="例如：復古拍立得風格、讓圖片模糊一點...")
        
        if st.button("✨ 開始處理", type="primary", use_container_width=True):
            if not user_text:
                st.warning("請輸入描述")
            else:
                with st.status("🚀 處理中...", expanded=True) as status:
                    # 1. AI 生成指令
                    st.write("正在分析需求...")
                    cmd = ai_engine.get_gmic_command(user_text)
                    
                    if "Error" in cmd:
                        status.update(label="❌ AI 生成失敗", state="error")
                        st.error(cmd)
                    else:
                        # 2. 執行 G'MIC
                        st.write(f"正在套用指令: `{cmd}`")
                        success, result, buf = gmic_processor.apply_effect(raw_img, cmd)
                        
                        if success:
                            st.session_state.processed_image = result
                            st.session_state.current_cmd = cmd
                            st.session_state.download_buffer = buf
                            status.update(label="✅ 處理完成", state="complete")
                        else:
                            status.update(label="❌ G'MIC 執行失敗", state="error")
                            st.error(result)

        # 手動除錯區塊
        with st.expander("🛠️ 進階：手動輸入 G'MIC 指令"):
            manual_cmd = st.text_input("參數", placeholder="-fx_pencil 10")
            if st.button("執行手動指令"):
                success, result, buf = gmic_processor.apply_effect(raw_img, manual_cmd)
                if success:
                    st.session_state.processed_image = result
                    st.session_state.current_cmd = manual_cmd
                    st.session_state.download_buffer = buf
                    st.success("執行成功")
                else:
                    st.error(result)

with col2:
    if st.session_state.processed_image:
        st.subheader("處理結果")
        st.code(f"gmic input {st.session_state.current_cmd} output", language="bash")
        st.image(st.session_state.processed_image, use_container_width=True)
        
        # 檔名處理
        safe_name = re.sub(r'[\\/*?:"<>| ]', "_", st.session_state.current_cmd)[:30]
        st.download_button(
            label="📥 下載處理後的圖片",
            data=st.session_state.download_buffer,
            file_name=f"ai_gmic_{safe_name}.jpg",
            mime="image/jpeg",
            use_container_width=True
        )
    else:
        st.info("👈 請在左側上傳圖片並輸入需求")