import requests
from bs4 import BeautifulSoup
import time
from urllib.parse import urljoin
import sys
import json
import os

# ================= 配置 =================
BASE_URL = "https://gmic.eu/reference/"
LIST_PAGE_URL = "https://gmic.eu/reference/list_of_commands.html"
RAW_DATA_FILE = "gmic_raw_data.json"

# 忽略清單 (只在下載階段做第一層過濾)
IGNORED_CATEGORIES = [
    "Global Options", "Input / Output", "List Manipulation", 
    "Mathematical Operators", "Matrix Computation", "3D Meshes", 
    "Flow Control", "Neural Networks", "Arrays, Tiles and Frames", 
    "Image Sequences and Videos", "Convenience Functions", 
    "Other Interactive Commands", "Command Shortcuts"
]

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

def get_soup(url):
    try:
        response = requests.get(url, headers=HEADERS, timeout=10)
        response.raise_for_status()
        response.encoding = 'utf-8'
        return BeautifulSoup(response.text, "html.parser")
    except Exception as e:
        print(f"Error fetching {url}: {e}")
        return None

def main():
    if os.path.exists(RAW_DATA_FILE):
        print(f"⚠️ 警告: {RAW_DATA_FILE} 已存在。若要重新下載請先刪除它。")
        # 您可以選擇在這裡直接 return，或是覆蓋
    
    print(f"正在讀取列表: {LIST_PAGE_URL}")
    soup = get_soup(LIST_PAGE_URL)
    if not soup: sys.exit("無法讀取列表")

    content_area = soup.find("div", class_="content")
    headers = content_area.find_all("h1", class_="ref_h1")
    
    tasks = [] # 待下載清單
    
    print("--- 分析分類中 ---")
    for header in headers:
        cat_name = header.get_text(strip=True).replace(":", "")
        if cat_name in ["List of Commands", "Categories"]: continue
            
        # 檢查忽略
        if any(ig.lower() in cat_name.lower() for ig in IGNORED_CATEGORIES):
            continue
            
        # 找到該分類下的表格
        cmd_table = header.find_next("table", class_="ref_table_category")
        if cmd_table:
            links = cmd_table.find_all("a")
            for link in links:
                href = link.get('href')
                name = link.text.strip()
                if not name and link.find("span"): name = link.find("span").text.strip()
                
                if href and not href.startswith("#") and "index.html" not in href:
                    full_url = urljoin(BASE_URL, href)
                    tasks.append({
                        "name": name,
                        "category": cat_name,
                        "url": full_url
                    })

    print(f"共發現 {len(tasks)} 個有效指令。開始下載原始 HTML...")
    
    data_store = []
    
    for i, task in enumerate(tasks):
        print(f"[{i+1}/{len(tasks)}] 下載中: {task['name']} ...")
        
        detail_soup = get_soup(task['url'])
        
        if detail_soup:
            # 我們只存取 content 區塊的 HTML 字串，節省空間並保留所有資訊供後續處理
            content_div = detail_soup.find("div", class_="content")
            if content_div:
                data_store.append({
                    "name": task['name'],
                    "category": task['category'],
                    "url": task['url'],
                    "raw_html": str(content_div) # 存成字串
                })
        
        time.sleep(0.2) 

    # 儲存到 JSON
    with open(RAW_DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data_store, f, ensure_ascii=False, indent=2)
        
    print(f"\n✅ 下載完成！原始資料已儲存至 {RAW_DATA_FILE}")
    print("現在你可以執行 'step2_process.py' 來生成 Markdown。")

if __name__ == "__main__":
    main()