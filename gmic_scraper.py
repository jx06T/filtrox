import requests
from bs4 import BeautifulSoup
from markdownify import markdownify as md
import time
from urllib.parse import urljoin
import sys

# ================= 配置區域 =================
BASE_URL = "https://gmic.eu/reference/"
LIST_PAGE_URL = "https://gmic.eu/reference/list_of_commands.html"
OUTPUT_FILE = "gmic_commands_lr_focused.md"

# 定義要忽略的類別 (根據您提供的 HTML 內容更新)
# 這些是我們不希望 AI 學習的非修圖類指令
IGNORED_CATEGORIES = [
    "Global Options",             # 系統設定，與修圖無關
    "Input / Output",             # 讀寫檔案由 Python 處理，不讓 AI 插手
    "List Manipulation",          # 堆疊操作，太底層
    "Mathematical Operators",     # 純數學運算
    "Matrix Computation",         # 矩陣運算
    "3D Meshes",                  # 3D 模型
    "Flow Control",               # 程式迴圈邏輯
    "Neural Networks",            # 神經網路
    "Arrays, Tiles and Frames",   # 陣列操作
    "Image Sequences and Videos", # 影片處理
    "Convenience Functions",      # 系統工具
    "Other Interactive Commands", # 互動式 demo
    "Command Shortcuts"           # 縮寫表，不需要
]

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

# ================= 核心邏輯 =================

def get_soup(url):
    """發送請求並回傳 BeautifulSoup 物件"""
    try:
        response = requests.get(url, headers=HEADERS, timeout=10)
        response.raise_for_status()
        response.encoding = 'utf-8'
        return BeautifulSoup(response.text, "html.parser")
    except Exception as e:
        print(f"Error fetching {url}: {e}")
        return None

def clean_content(soup_content):
    """清理單頁詳情內的 HTML 雜訊"""
    if not soup_content:
        return ""

    # 移除導航列、Script、Style
    for tag in soup_content.select("table.ref_navigation_top, div.ref_navigation_bottom, script, style"):
        tag.decompose()

    # 移除回到頂部的錨點
    for a in soup_content.find_all("a", href="#top"):
        a.decompose()
        
    # 移除 immersive-translate 產生的翻譯標籤 (如果您是爬原始網頁通常不會有，但以防萬一)
    for tag in soup_content.find_all(attrs={"class": "immersive-translate-target-wrapper"}):
        tag.decompose()

    return soup_content

def process_detail_page(url):
    """處理單個指令頁面並轉為 Markdown"""
    soup = get_soup(url)
    if not soup:
        return None

    content_div = soup.find("div", class_="content")
    if not content_div:
        return None

    cleaned_soup = clean_content(content_div)
    # 使用 ATX 風格 (#) 標題
    return md(str(cleaned_soup), heading_style="ATX").strip()

def main():
    print(f"正在讀取指令列表頁面: {LIST_PAGE_URL}")
    soup = get_soup(LIST_PAGE_URL)
    
    if not soup:
        sys.exit("無法讀取列表頁面")

    # 修正後的選擇器邏輯：
    # 1. 鎖定 content 區域
    content_area = soup.find("div", class_="content")
    
    # 2. 抓取所有 h1 且 class 為 ref_h1 的標籤 (這是分類標題)
    headers = content_area.find_all("h1", class_="ref_h1")
    
    valid_links = []
    
    print(f"--- 開始分析分類 ---")
    
    for header in headers:
        # 清理標題文字：移除冒號和前後空白 (例如 "Colors:" -> "Colors")
        cat_name = header.get_text(strip=True).replace(":", "")
        
        # 跳過非指令分類的標題
        if cat_name in ["List of Commands", "Categories"]:
            continue
            
        # 檢查是否在忽略清單中
        is_ignored = False
        for ignore_keyword in IGNORED_CATEGORIES:
            # 寬鬆比對：只要分類名稱包含黑名單關鍵字就跳過
            if ignore_keyword.lower() == cat_name.lower() or ignore_keyword in cat_name:
                is_ignored = True
                break
        
        if is_ignored:
            print(f"❌ [忽略分類] {cat_name}")
            continue
        
        print(f"✅ [保留分類] {cat_name}")
        
        # 3. 尋找該標題對應的表格
        # find_next 會往下尋找最近的一個 table (class 為 ref_table_category)
        cmd_table = header.find_next("table", class_="ref_table_category")
        
        if cmd_table:
            links = cmd_table.find_all("a")
            for link in links:
                href = link.get('href')
                name = link.text.strip()
                
                # 過濾有效連結
                if href and not href.startswith("#") and "index.html" not in href:
                    # 有些連結包含 span 標籤造成的雜訊，再次清理 name
                    # (例如: <span class="gmd_monospace">append</span>)
                    if not name: 
                        name = link.find("span").text.strip() if link.find("span") else "Unknown"

                    valid_links.append({
                        "name": name,
                        "url": urljoin(BASE_URL, href),
                        "category": cat_name
                    })

    print(f"\n--- 篩選完成 ---")
    print(f"共找到 {len(valid_links)} 個符合 LR 風格的指令。開始爬取詳情...\n")

    # 開啟檔案寫入
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write("# G'MIC Command Reference for AI Photo Editing\n")
        f.write("This dataset is filtered for commands related to Colors, Filtering, Geometry, and Artistic effects.\n\n")

        for i, item in enumerate(valid_links):
            print(f"[{i+1}/{len(valid_links)}] 爬取: {item['name']} (分類: {item['category']})")
            
            content_md = process_detail_page(item['url'])
            
            if content_md:
                f.write(f"\n\n---\n\n")
                f.write(f"# Command: {item['name']}\n")
                f.write(f"**Category:** {item['category']}\n")
                f.write(f"**Source:** {item['url']}\n\n")
                f.write(content_md)
                f.flush()
            
            # 避免對伺服器造成過大壓力
            time.sleep(0.1)

    print(f"\n全部完成！已儲存至 {OUTPUT_FILE}")

if __name__ == "__main__":
    main()