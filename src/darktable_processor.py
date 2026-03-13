import os
from .xmp_gen import gen


class DarktableProcessor:
    def __init__(self, binary_path="darktable-cli"):
        self.binary_path = binary_path
  

    def apply_effect(self, input_path: str, ai_params: dict, output_path: str):
        final_output_path = gen(
            input_path,
            ai_params,
            output_path,
            darktable_cli_path=self.binary_path,
        )
        # return final_output_path

        # 檢查回傳值是否為字串路徑，且該路徑檔案真的存在
        if isinstance(final_output_path, str) and os.path.exists(final_output_path):
            return final_output_path
        
        # 如果失敗，回傳 None 或拋出異常，讓 app.py 知道不要去讀取圖片
        print(f"[DEBUG] apply_effect failed. Received from gen: {final_output_path}")
        return None

# ==========================================
# 測試區
# ==========================================
if __name__ == "__main__":
    proc = DarktableProcessor(binary_path="darktable-cli")
    
    # 測試：連續執行兩次，觀察檔名變化
    in_file = "IMG_1663.JPG" 
    target_path = "tt/result.jpg"
    
    params = {
        "global_C": -0.5, 
        
        "saturation_global": 0.0, 
        
        "global_Y": -0.5, 
        
        "saturation_formula": 1 
    }

    try:
        # 第一次執行 -> tt/result.jpg
        # 第二次執行 -> tt/result_01.jpg
        # 第三次執行 -> tt/result_02.jpg
        actual_path = proc.apply_effect(in_file, params, target_path)
        print(f"✨ 渲染完成！最終檔案儲存於: {actual_path}")
    except Exception as e:
        print(f"❌ 發生錯誤: {e}")
