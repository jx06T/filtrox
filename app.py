import streamlit as st
import google.generativeai as genai
import subprocess
import os
import tempfile
from PIL import Image
from pathlib import Path
from dotenv import load_dotenv
load_dotenv()

# ================= 配置區域 =================
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=GEMINI_API_KEY)
print(GEMINI_API_KEY)

GMIC_PATH = Path(__file__).parent / "gmic"

# ================= 定義 G'MIC 指令參考 (給 AI 的知識庫) =================
# 這裡定義你希望系統支援的效果，以及對應的 G'MIC 語法
# 為了安全和準確，建議限制 AI 只能從這裡參考或組合
GMIC_REFERENCE = """
你是一個 G'MIC 指令產生器。你的任務是根據使用者的描述，從以下列表中選擇最合適的指令並調整參數。
只輸出指令參數字串，不要輸出任何解釋、Markdown 或程式碼區塊。

可用指令參考 (Reference):
1. 黑白素描 (Sketch): -fx_pencil 10,0 (參數範圍 0-100)
2. 拍立得效果 (Polaroid): -fx_polaroid 10,0
3. 舊照片/復古 (Old Photo): -fx_old_photo 0,0,0
4. 夢幻平滑/油畫感 (Dream/Oil): -fx_dream_smoothing 10,0,1
5. 高斯模糊 (Blur): -blur 3 (參數: 強度)
6. 銳化 (Sharpen): -sharpen 100
7. 卡通化 (Cartoon): -fx_cartoon 0,0
8. 增加對比度 (Contrast): -adjust_colors 0,20,0,0 (參數: 亮度,對比,伽瑪,色相)
9. 水彩畫 (Watercolor): -fx_watercolor 0.3,0

規則:
- 如果使用者要求稍微強一點，請適度調整數值。
- 如果使用者說的話與圖片處理無關，回傳 "INVALID"。
- 輸出格式範例: -fx_pencil 20,0
"""

# ================= AI 處理邏輯 =================
def get_gmic_command_from_gemini(user_prompt):
    model = genai.GenerativeModel('gemini-1.5-flash') # 使用 Flash 模型速度較快
    
    full_prompt = f"{GMIC_REFERENCE}\n\n使用者需求: {user_prompt}\n輸出的 G'MIC 參數:"
    
    try:
        response = model.generate_content(full_prompt)
        command = response.text.strip()
        # 清除可能的 markdown 符號
        command = command.replace("`", "").replace("\n", "")
        return command
    except Exception as e:
        return f"Error: {e}"

# ================= G'MIC 執行邏輯 =================
def apply_gmic_effect(input_image_path, output_image_path, gmic_args):
    """
    使用 subprocess 呼叫系統的 gmic 指令
    """
    # 組合完整指令: gmic input.jpg [參數] -o output.jpg
    # 注意：這裡使用 shlex.split 可能更安全，但為了簡單演示直接組裝 list
    # 我們將指令拆解以避免 Shell Injection (雖然參數來自 Gemini，但仍需小心)
    
    cmd = [str(GMIC_PATH), input_image_path] + gmic_args.split() + ["-o", output_image_path]
    
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        return True, result.stdout
    except subprocess.CalledProcessError as e:
        return False, e.stderr
    except FileNotFoundError:
        return False, "找不到 'gmic' 指令，請確認是否已安裝並加入環境變數 PATH 中。"

# ================= Streamlit UI 介面 =================
st.title("🎨 AI 自然語言修圖助手 (G'MIC)")
st.caption("Powered by Gemini & G'MIC")

uploaded_file = st.file_uploader("上傳一張圖片", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    # 1. 顯示原圖
    image = Image.open(uploaded_file)
    st.image(image, caption="原始圖片", use_container_width=True)
    
    # 2. 儲存暫存檔 (因為 G'MIC CLI 需要實體檔案路徑)
    with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as tmp_in:
        image = image.convert('RGB') # 轉為 RGB 避免 PNG 透明度問題
        image.save(tmp_in.name)
        input_path = tmp_in.name

    # 3. 使用者輸入
    user_text = st.text_input("你想怎麼修改這張圖？", placeholder="例如：把它變成一張復古的拍立得照片")

    if st.button("開始生成") and user_text:
        with st.spinner("Gemini 正在思考 G'MIC 參數..."):
            # A. 取得指令
            gmic_params = get_gmic_command_from_gemini(user_text)
            
            if gmic_params == "INVALID":
                st.error("無法理解您的需求，請描述圖片處理相關的指令。")
            elif "Error" in gmic_params:
                st.error(gmic_params)
            else:
                st.success(f"生成的指令: `{gmic_params}`")
                
                # B. 執行 G'MIC
                with st.spinner("G'MIC 正在渲染圖片..."):
                    with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as tmp_out:
                        output_path = tmp_out.name
                    
                    success, log = apply_gmic_effect(input_path, output_path, gmic_params)
                    
                    if success:
                        processed_image = Image.open(output_path)
                        st.image(processed_image, caption="處理後結果", use_container_width=True)
                        
                        # 下載按鈕
                        with open(output_path, "rb") as file:
                            btn = st.download_button(
                                label="下載圖片",
                                data=file,
                                file_name="processed_image.jpg",
                                mime="image/jpeg"
                            )
                    else:
                        st.error(f"G'MIC 執行失敗: {log}")
                    
                    # 清理輸出暫存檔
                    if os.path.exists(output_path):
                        os.remove(output_path)

    # 清理輸入暫存檔
    if os.path.exists(input_path):
        os.remove(input_path)