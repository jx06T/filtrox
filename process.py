import json
from bs4 import BeautifulSoup
from markdownify import markdownify as md
import os
import re

# ================= 配置 =================
INPUT_FILE = "gmic_raw_data.json"
OUTPUT_FILE = "gmic_commands_final.md"

def clean_html(html_str):
    soup = BeautifulSoup(html_str, "html.parser")
    
    # 1. 移除導航、樣式、腳本
    for tag in soup.select("table.ref_navigation_top, div.ref_navigation_bottom, script, style"):
        tag.decompose()

    # 2. 移除重複的 h1 標題
    for h1 in soup.find_all("h1"):
        h1.decompose()

    # 3. 移除錨點
    for a in soup.find_all("a", href="#top"):
        a.decompose()

    # 4. 移除所有圖片與展示區塊
    for tag in soup.select("img, div.center, div.highslide-caption, a.highslide"):
        # 注意：這次我們要更徹底，只要是展示用的 a.highslide 全部刪掉
        # 真正代碼區塊裡的連結我們會在下面用特殊邏輯處理
        if tag.name == 'a' and tag.find_parent(class_="gmd_code_block"):
            continue
        tag.decompose()

    # 5. 移除 "Example of use" 標題
    for h2 in soup.find_all("h2"):
        if "Example of use" in h2.get_text():
            h2.decompose()

    # 6. [終極修正] 處理代碼區塊 - 解決 HTML Escaping 問題
    for block in soup.find_all("div", class_="gmd_code_block"):
        # 步驟 A: 獲取文字內容。
        # 因為網頁原始碼是用 &lt;a href...&gt;，get_text() 會把它轉回 <a href...> 字串
        escaped_content = block.get_text()
        
        # 步驟 B: [關鍵] 二次解析
        # 將含有 HTML 標籤字串的內容再次解析，這樣 BeautifulSoup 才能識別出 <a> 標籤
        inner_soup = BeautifulSoup(escaped_content, "html.parser")
        
        # 步驟 C: 現在可以乾淨地提取純文字了 (會自動丟棄 <a> 標籤)
        clean_code = inner_soup.get_text(" ", strip=True)
        
        # 步驟 D: 清理多餘空白
        clean_code = " ".join(clean_code.split())
        
        # 步驟 E: 加上 CLI 前綴
        full_command = f"gmic {clean_code}"
        
        # 步驟 F: 重建 Markdown 代碼塊結構
        new_pre = soup.new_tag("pre")
        new_code = soup.new_tag("code", attrs={"class": "language-bash"})
        new_code.string = full_command
        new_pre.append(new_code)
        
        block.replace_with(new_pre)

    # 7. 移除翻譯插件雜訊
    for tag in soup.find_all(attrs={"class": "immersive-translate-target-wrapper"}):
        tag.decompose()

    return soup

def convert_to_markdown(soup):
    text = md(str(soup), heading_style="ATX", strip=['img'])
    
    # 還原被轉義的底線
    text = text.replace(r"\_", "_")

    # 清理多餘空行
    lines = [line.strip() for line in text.splitlines()]
    clean_text = []
    for line in lines:
        if line or (clean_text and clean_text[-1]):
            clean_text.append(line)
            
    return "\n".join(clean_text).strip()

def main():
    if not os.path.exists(INPUT_FILE):
        print(f"找不到 {INPUT_FILE}")
        return

    print(f"正在讀取原始資料: {INPUT_FILE} ...")
    with open(INPUT_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)

    print(f"開始處理 {len(data)} 筆資料...")
    
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write("# G'MIC Command Reference\n\n")
        
        for item in data:
            cleaned_soup = clean_html(item['raw_html'])
            md_content = convert_to_markdown(cleaned_soup)
            
            if md_content:
                f.write("\n---\n\n")
                f.write(f"# Command: {item['name']}\n\n")
                f.write(md_content)
                f.write("\n")
    
    print(f"✅ 處理完成！結果已儲存至 {OUTPUT_FILE}")

if __name__ == "__main__":
    main()