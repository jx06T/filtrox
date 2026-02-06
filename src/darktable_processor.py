import os
import subprocess
import tempfile
from .dt_patcher import XMPPatcher

# 使用您提供的、確定可運作的完整 XMP 作為模板
DEFAULT_XMP_TEMPLATE = """<?xml version="1.0" encoding="UTF-8"?>
<x:xmpmeta xmlns:x="adobe:ns:meta/" x:xmptk="XMP Core 4.4.0-Exiv2">
 <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
  <rdf:Description rdf:about=""
    xmlns:darktable="http://darktable.sf.net/"
   darktable:xmp_version="5"
   darktable:history_end="5"
   darktable:iop_order_version="5">
   <darktable:history>
    <rdf:Seq>
     <rdf:li darktable:num="0" darktable:operation="colorin" darktable:enabled="1" darktable:modversion="7" darktable:params="gz48eJzjZBgFowABWAbaAaNgwAEAMNgADg==" />
     <rdf:li darktable:num="1" darktable:operation="colorout" darktable:enabled="1" darktable:modversion="5" darktable:params="gz35eJxjZBgFo4CBAQAEEAAC" />
     <rdf:li darktable:num="2" darktable:operation="gamma" darktable:enabled="1" darktable:modversion="1" darktable:params="0000000000000000" />
     <rdf:li darktable:num="3" darktable:operation="flip" darktable:enabled="1" darktable:modversion="2" darktable:params="ffffffff" />
     <rdf:li darktable:num="4" darktable:operation="colorbalancergb" darktable:enabled="1" darktable:modversion="5" darktable:params="gz04eJxjYGiwZ2BAQA4DgwM2BdF8fQA2xwVn" />
    </rdf:Seq>
   </darktable:history>
  </rdf:Description>
 </rdf:RDF>
</x:xmpmeta>
"""

# (DEFAULT_XMP_TEMPLATE 保持不變...)

class DarktableProcessor:
    def __init__(self, binary_path="darktable-cli"):
        self.binary_path = binary_path

    def _get_unique_path(self, path: str) -> str:
        """
        如果檔案已存在，則產生一個新的序號檔名 (例如 result.jpg -> result_01.jpg)
        """
        if not os.path.exists(path):
            return path
        
        base, ext = os.path.splitext(path)
        counter = 1
        
        # 循環直到找到一個不存在的檔名
        while True:
            # 使用 :02d 讓編號變成 _01, _02 比較美觀
            new_path = f"{base}_{counter:02d}{ext}"
            if not os.path.exists(new_path):
                return new_path
            counter += 1

    def apply_effect(self, input_path: str, ai_params: dict, output_path: str):
        if not os.path.exists(input_path):
            raise FileNotFoundError(f"找不到輸入檔案: {input_path}")
            
        # 確保目錄存在
        os.makedirs(os.path.dirname(output_path) if os.path.dirname(output_path) else ".", exist_ok=True)

        # === 核心改變：取得一個不衝突的唯一路徑 ===
        final_output_path = self._get_unique_path(output_path)

        with tempfile.TemporaryDirectory() as temp_dir:
            temp_xmp = os.path.join(temp_dir, "recipe.xmp")

            patch_config = {
                "colorbalancergb": {
                    "enabled": 1,
                    "params": ai_params
                }
            }
            final_xmp_content = XMPPatcher.patch_xmp_content(DEFAULT_XMP_TEMPLATE, patch_config)
            
            with open(temp_xmp, "w", encoding="utf-8") as f:
                f.write(final_xmp_content)

            # 執行 Darktable CLI，使用我們計算出的 final_output_path
            cmd = [
                self.binary_path, 
                input_path, 
                temp_xmp, 
                final_output_path,
                "--core",             # <--- 關鍵：5.x 版後的核心參數分隔符
                "--library", ":memory:",
                "--disable-opencl"
                ]
            print(f"🎨 正在渲染至: {final_output_path}")
            
            try:
                result = subprocess.run(
                    cmd, 
                    capture_output=True, 
                    text=True,
                    timeout=60
                )
                
                # 印出標準輸出，有時候錯誤會噴在這裡
                if result.stdout:
                    print(f"--- Darktable STDOUT ---\n{result.stdout}")
                
            except subprocess.CalledProcessError as e:
                # 即使出錯也印出 stdout 和 stderr
                print(f"--- Darktable ERROR ---\nSTDOUT: {e.stdout}\nSTDERR: {e.stderr}")
                raise RuntimeError(f"Darktable CLI 失敗: {e.stderr}")

            # 如果回傳碼不是 0，代表失敗了
            if result.returncode != 0:
                error_msg = result.stderr if result.stderr else "未知錯誤 (可能是程式閃退或 OpenCL 崩潰)"
                # 同時檢查 stdout
                if not result.stderr and result.stdout:
                    error_msg = f"Stdout 中可能有線索: {result.stdout}"
                
                raise RuntimeError(f"Darktable 失敗 (代碼 {result.returncode}):\n{error_msg}")
            
                 # 回傳最終產生的檔案路徑，讓調用者知道檔名變成了什麼
            return final_output_path

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

