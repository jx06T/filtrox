import streamlit as st
import google.generativeai as genai
import subprocess
import os
import tempfile
import io
import re
from PIL import Image
from pathlib import Path

# ================= 配置區域 =================
st.set_page_config(page_title="AI G'MIC 修圖", layout="wide")

try:
    GEMINI_API_KEY = st.secrets["GEMINI_API_KEY"]
except:
    st.error("請在 .streamlit/secrets.toml 中設定 GEMINI_API_KEY")
    st.stop()

genai.configure(api_key=GEMINI_API_KEY)

# 設定 G'MIC 路徑
GMIC_PATH = Path(__file__).parent / "gmic" / "gmic" 

# 設定參考文件路徑
REFERENCE_FILE = Path(__file__).parent / "gmic_commands_final.md"

# ================= 1. 初始化 Session State =================
if 'processed_image' not in st.session_state:
    st.session_state.processed_image = None
if 'generated_cmd' not in st.session_state:
    st.session_state.generated_cmd = None
if 'download_buffer' not in st.session_state:
    st.session_state.download_buffer = None

# ================= 2. 讀取參考文件 (RAG) =================
@st.cache_data
def load_reference_data():
    if REFERENCE_FILE.exists():
        return REFERENCE_FILE.read_text(encoding="utf-8")
    else:
        return ""

reference_content = load_reference_data()

if not reference_content:
    GMIC_KNOWLEDGE_BASE = """
    可用指令範例:
    -fx_pencil 10,0 (素描)
    -fx_polaroid 10,0 (拍立得)
    -blur 3 (模糊)
    """
else:
    GMIC_KNOWLEDGE_BASE = reference_content

# ================= AI 處理邏輯 =================
def get_gmic_command_from_gemini(user_prompt):
    # model = genai.GenerativeModel('gemini-2.5-flash-lite') 
    model = genai.GenerativeModel('gemini-2.5-flash') 
    
    system_prompt = f"""
    你是一個 G'MIC 指令轉換專家。
    請閱讀以下 G'MIC 指令參考文件，並根據使用者的自然語言需求，生成對應的 G'MIC 參數。

    --- 參考文件開始 ---
    {GMIC_KNOWLEDGE_BASE}
    --- 參考文件結束 ---

    規則：
    1. **只輸出參數部分**，不需要 `gmic` 開頭，也不需要 `input.jpg` 或 `-o output.jpg`。
    2. 例如使用者說「我要素描感」，參考文件若顯示 `gmic img.jpg -fx_pencil 10`，你只需輸出 `-fx_pencil 10`(請注意若要使用預設參數也需要完整的給出參數)。
    3. 如果需要組合多個效果，請用空格分隔，例如 `-blur 2 -sharpen 50`。
    4. 不要輸出 Markdown 程式碼符號 (如 ```bash)。
    5. 務必確認每一個使用的指令都是在文件提到的，有些效果需要嘗試使用不同參數組合來達成。
    """
    
    chat = model.start_chat(history=[])
    try:
        response = chat.send_message(f"{system_prompt}\n\n使用者需求: {user_prompt}")
        command = response.text.strip()
        command = command.replace("`", "").replace("bash", "").strip()
        if command.startswith("gmic "):
            command = command[5:]
        return command
    except Exception as e:
        return f"Error: {e}"

# ================= G'MIC 執行邏輯 =================
def apply_gmic_effect(input_image, gmic_args):
    with tempfile.NamedTemporaryFile(delete=False, suffix=".png") as tmp_in:
        input_image.save(tmp_in, format="PNG")
        input_path = tmp_in.name
    
    output_path = input_path.replace(".png", "_out.png")

    try:
        cmd_base = str(GMIC_PATH)
        args_list = gmic_args.split()
        
        # 強制只保留最後一張圖 -keep[-1]
        full_cmd = [cmd_base, input_path] + args_list + ["-keep[-1]", "-o", output_path]
        
        print(f"Executing: {' '.join(full_cmd)}")

        result = subprocess.run(full_cmd, capture_output=True, text=True)

        if result.returncode != 0:
            return False, f"G'MIC 指令錯誤 (Code {result.returncode}):\n{result.stderr}", None

        if os.path.exists(output_path):
            try:
                result_img = Image.open(output_path).convert("RGB")
                buf = io.BytesIO()
                result_img.save(buf, format="JPEG", quality=95)
                buf.seek(0)
                result_img.load()
                return True, result_img, buf
            except Exception as e:
                return False, f"無法讀取圖片: {str(e)}", None
        else:
            return False, f"找不到輸出檔案: {output_path}\nLog: {result.stderr}", None

    except Exception as e:
        return False, f"系統錯誤: {str(e)}", None

    finally:
        try:
            if os.path.exists(input_path): os.remove(input_path)
            if os.path.exists(output_path): os.remove(output_path)
            base_out = output_path.replace(".png", "")
            folder = os.path.dirname(output_path)
            for f in os.listdir(folder):
                if f.startswith(os.path.basename(base_out)) and f.endswith(".png"):
                    try: os.remove(os.path.join(folder, f))
                    except: pass
        except: pass

# ================= Streamlit UI 介面 =================
st.title("🎨 AI 自然語言修圖助手 (G'MIC RAG版)")

col1, col2 = st.columns([1, 1.5])

with col1:
    uploaded_file = st.file_uploader("上傳一張圖片", type=["jpg", "png", "jpeg"])
    
    if uploaded_file is not None:
        image = Image.open(uploaded_file).convert("RGB")
        st.image(image, caption="原始圖片", use_container_width=True)
        
        # --- AI 生成區塊 ---
        st.divider()
        st.subheader("🤖 AI 自動生成")
        user_text = st.text_area("描述需求", height=80, placeholder="例如：復古拍立得風格...")
        
        if st.button("✨ AI 生成", type="primary", use_container_width=True):
            if not user_text:
                st.warning("請輸入描述")
            else:
                with st.status("🚀 AI 處理中...", expanded=True) as status:
                    gmic_params = get_gmic_command_from_gemini(user_text)
                    if "Error" in gmic_params or gmic_params == "INVALID":
                        status.update(label="❌ 發生錯誤", state="error")
                        st.error(f"AI 生成失敗: {gmic_params}")
                    else:
                        st.write(f"🔧 指令: `{gmic_params}`")
                        success, res_img, res_buf = apply_gmic_effect(image, gmic_params)
                        if success:
                            st.session_state.processed_image = res_img
                            st.session_state.generated_cmd = gmic_params
                            st.session_state.download_buffer = res_buf
                            status.update(label="✅ 完成！", state="complete")
                        else:
                            status.update(label="❌ G'MIC 失敗", state="error")
                            st.error(res_img)

        # --- 手動 Debug 區塊 ---
        st.divider()
        with st.expander("🛠️ 開發者除錯模式 (手動輸入)", expanded=False):
            st.caption("直接輸入 G'MIC 參數 (不含 `gmic input output`)")
            manual_cmd = st.text_input("G'MIC 參數", placeholder="-fx_pencil 10 -blur 1")
            
            if st.button("🔧 執行手動指令", use_container_width=True):
                if not manual_cmd:
                    st.warning("請輸入參數")
                else:
                    with st.spinner("執行手動指令中..."):
                        success, res_img, res_buf = apply_gmic_effect(image, manual_cmd)
                        if success:
                            st.session_state.processed_image = res_img
                            st.session_state.generated_cmd = manual_cmd # 標記為手動指令
                            st.session_state.download_buffer = res_buf
                            st.success(f"執行成功: `{manual_cmd}`")
                        else:
                            st.error(f"執行失敗:\n{res_img}")

# 右側：顯示結果
with col2:
    if st.session_state.processed_image is not None:
        st.subheader("處理結果")
        
        # 顯示當前使用的指令
        current_cmd = st.session_state.generated_cmd
        st.code(f"gmic input {current_cmd} output", language="bash")
        
        st.image(st.session_state.processed_image, caption="修圖結果", use_container_width=True)
        
        # 處理檔名 (移除不合法字元，避免下載時檔名錯誤)
        safe_filename = re.sub(r'[\\/*?:"<>|]', "", current_cmd)
        safe_filename = safe_filename.replace(" ", "_")[:50] # 限制長度
        
        if st.session_state.download_buffer:
            st.download_button(
                label="📥 下載圖片",
                data=st.session_state.download_buffer,
                file_name=f"gmic_{safe_filename}.jpg",
                mime="image/jpeg",
                use_container_width=True
            )
    else:
        if uploaded_file:
            st.info("👈 請在左側使用 AI 生成或手動輸入指令")
        else:
            st.info("👈 請先上傳圖片")