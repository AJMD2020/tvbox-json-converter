import requests
from bs4 import BeautifulSoup
import json

# 1. 抓取网页内容
url = "https://www.ikunzy.com/"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# 2. 提取影视数据（需根据实际HTML结构调整）
movies = []
for item in soup.select('.movie-list li'):
    title = item.select_one('.title').text
    cover = item.select_one('img')['src']
    play_url = item.select_one('a')['href']
    
    movies.append({
        "id": play_url.split('/')[-1],  # 假设URL包含ID
        "name": title,
        "pic": cover,
        "url": f"csp_{play_url}",       # 添加解析规则
        "type_id": 1                    # 分类ID（需自定义）
    })

# 3. 生成影视仓兼容JSON
output = {
    "class": [{"type_id": 1, "type_name": "电影"}],
    "list": movies
}

# 4. 保存文件
with open('output.json', 'w', encoding='utf-8') as f:
    json.dump(output, f, ensure_ascii=False)
