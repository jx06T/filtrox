import subprocess
import os
import tempfile
import io
import shlex  # 關鍵：用於正確解析複雜的命令行參數
from PIL import Image
from pathlib import Path

class GMICProcessor:
    def __init__(self, gmic_binary_path: Path):
        self.gmic_path = str(gmic_binary_path)

    def apply_effect(self, input_image: Image.Image, gmic_args: str):
        # 1. 建立暫存檔案
        with tempfile.NamedTemporaryFile(delete=False, suffix=".png") as tmp_in:
            input_image.save(tmp_in, format="PNG")
            input_path = tmp_in.name
        output_path = input_path.replace(".png", "_out.png")

        try:
            # 2. 使用 shlex 解析指令字串 (避免 .split() 造成的語法錯誤)
            # 例如: '-blur 5' 變成 ['-blur', '5']
            try:
                args_list = shlex.split(gmic_args)
            except ValueError:
                # 如果 shlex 解析失敗（例如引號沒閉合），退回普通 split
                args_list = gmic_args.split()

            # 3. 組合完整指令
            full_cmd = [self.gmic_path, input_path] + args_list + ["-keep[-1]", "-o", output_path]
            
            # 除錯用：在後台印出實際執行的完整指令
            print(f"Executing: {' '.join(full_cmd)}")

            # 4. 執行指令並加入超時限制 (Timeout)
            result = subprocess.run(
                full_cmd, 
                capture_output=True, 
                text=True, 
                timeout=45  # 限制最多跑 45 秒，防止伺服器卡死
            )

            if result.returncode != 0:
                return False, f"G'MIC 指令錯誤:\n{result.stderr}", None

            # 5. 讀取結果
            if os.path.exists(output_path):
                result_img = Image.open(output_path).convert("RGB")
                result_img.load() # 強制加載到記憶體
                
                buf = io.BytesIO()
                result_img.save(buf, format="JPEG", quality=95)
                buf.seek(0)
                return True, result_img, buf
            
            return False, "找不到輸出檔案，可能是指令未產生有效結果。", None

        # except subprocess.TimeoutExpired:
        #     return False, f"系統錯誤(已超時): {str(e)}", None
        except Exception as e:
            return False, f"系統錯誤: {str(e)}", None
        finally:
            # 6. 清理
            self._cleanup(input_path, output_path)

    def _cleanup(self, *files):
        for f in files:
            try:
                if os.path.exists(f):
                    os.remove(f)
                # 清理 G'MIC 可能產生的多個編號檔案
                base = os.path.basename(os.path.splitext(f)[0])
                directory = os.path.dirname(f)
                if directory:
                    for extra in os.listdir(directory):
                        if extra.startswith(base) and extra.endswith(".png"):
                            os.remove(os.path.join(directory, extra))
            except:
                pass