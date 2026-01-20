import os
import sys
from photo_editing_agent import PhotoEditingAgent
from darktable_processor import DarktableProcessor
from dotenv import load_dotenv
from llm_backend import BaseLLM , Gemini


load_dotenv()  
# ================= 設定區 =================
API_KEY = os.getenv("GEMINI_API_KEY")
INPUT_IMAGE = "IMG_1663.jpg"        # 請確保此檔案存在於同一目錄
CLI_PATH = "darktable-cli"       # 請確保 darktable-cli 在 PATH 中，或填寫絕對路徑
# ==========================================

def main():
    # 0. 檢查環境
    if not os.path.exists(INPUT_IMAGE):
        print(f"❌ 錯誤: 找不到測試圖片 {INPUT_IMAGE}，請隨便放一張 JPG 或 RAW 檔在根目錄。")
        return

    # 1. 初始化 AI
    print("🤖 初始化 AI Agent...")
    try:
        llm_service = Gemini(api_key=API_KEY)
        agent = PhotoEditingAgent(llm_provider=llm_service)

    except Exception as e:
        print(f"❌ AI 初始化失敗 (請檢查 API Key): {e}")
        return

    # 2. 初始化 處理器
    processor = DarktableProcessor(binary_path=CLI_PATH)

    # 3. 模擬使用者需求
    # user_request = "給我一種賽博龐克風格，強烈對比，霓虹感"
    user_request = "給我像是復古的膠片風格"
    print(f"🗣️ 使用者需求: {user_request}")

    # 4. AI 生成參數
    print("🧠 AI 正在思考參數...")
    variations = agent.cold_start(user_request)
    
    if not variations:
        print("❌ AI 生成失敗，未回傳有效參數。")
        return

    print(f"✅ AI 生成了 {len(variations)} 組方案。")

    # 5. 執行第一組方案
    target_var = variations[0]
    print(f"👉 選擇方案 1: {target_var['name']}")
    print(f"   參數: {target_var['parameters']}")
    
    # target_var = {'parameters':{'contrast': 0.35, 'shadows_Y': -0.15, 'shadows_C': 0.15, 'shadows_H': 220, 'midtones_C': 0.2, 'midtones_H': 300, 'highlights_Y': 0.1, 'highlights_C': 0.25, 'highlights_H': 330, 'vibrance': 0.2, 'saturation_global': 1.1}}

    output_filename = r"ai/output_result.jpg"
    
    try:
        print("🎨 開始渲染圖片...")
        processor.apply_effect(
            input_path=INPUT_IMAGE,
            ai_params=target_var['parameters'],
            output_path=output_filename
        )
        print(f"✨ 成功！結果已存為: {output_filename}")
        
    except Exception as e:
        print(f"❌ 渲染失敗: {e}")
        print("提示: 請確認有安裝 Darktable 並且 darktable-cli 指令可用。")

if __name__ == "__main__":
    main()