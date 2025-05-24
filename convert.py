import requests, json, os

SOURCE_URL = os.getenv('SOURCE_URL', 'https://ikunzyapi.com/api.php/provide/vod/at/json')
OUTPUT_FILE = 'output.json'

# 获取原始数据
response = requests.get(SOURCE_URL)
data = response.json()

# 字段映射转换
formatted_data = {
    "class": [
        {"type_id": cat["type_id"], "type_name": cat["type_name"]}
        for cat in data.get("class", [])
    ],
    "list": [
        {
            "id": item["vod_id"],
            "name": item["vod_name"],
            "pic": item["vod_pic"],
            "url": f"csp_{item['vod_url']}",
            "type_id": item["type_id"]
        } for item in data.get("list", [])
    ]
}

# 保存转换后数据
with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
    json.dump(formatted_data, f, ensure_ascii=False)
