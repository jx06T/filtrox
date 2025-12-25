import subprocess
import os
import tempfile
import io
from PIL import Image
from pathlib import Path

class GMICProcessor:
    def __init__(self, gmic_binary_path: Path):
        self.gmic_path = str(gmic_binary_path)

    def apply_effect(self, input_image: Image.Image, gmic_args: str):
        """執行 G'MIC 指令並回傳 (成功與否, 結果影像/錯誤訊息, 下載用的 Buffer)"""
        # 建立暫存檔
        with tempfile.NamedTemporaryFile(delete=False, suffix=".png") as tmp_in:
            input_image.save(tmp_in, format="PNG")
            input_path = tmp_in.name
        
        output_path = input_path.replace(".png", "_out.png")

        try:
            # 組合指令：[gmic, 輸入路徑, 使用者參數, 強制保留最後一張圖, 輸出路徑]
            args_list = gmic_args.split()
            full_cmd = [self.gmic_path, input_path] + args_list + ["-keep[-1]", "-o", output_path]
            
            result = subprocess.run(full_cmd, capture_output=True, text=True)

            if result.returncode != 0:
                return False, f"G'MIC Error: {result.stderr}", None

            if os.path.exists(output_path):
                result_img = Image.open(output_path).convert("RGB")
                # 預先加載到記憶體，避免檔案被刪除後無法讀取
                result_img.load() 
                
                # 準備下載用的 Buffer
                buf = io.BytesIO()
                result_img.save(buf, format="JPEG", quality=95)
                buf.seek(0)
                
                return True, result_img, buf
            else:
                return False, "Output file not found.", None

        except Exception as e:
            return False, f"System Error: {str(e)}", None

        finally:
            # 確保清理所有產生的暫存檔
            self._cleanup(input_path, output_path)

    def _cleanup(self, *files):
        for f in files:
            try:
                if os.path.exists(f):
                    os.remove(f)
                # 處理 G'MIC 可能產生的多個編號檔案 (例如 out_00001.png)
                base = os.path.splitext(f)[0]
                directory = os.path.dirname(f)
                if directory:
                    for extra in os.listdir(directory):
                        if extra.startswith(os.path.basename(base)) and extra.endswith(".png"):
                            os.remove(os.path.join(directory, extra))
            except:
                pass