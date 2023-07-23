import csv
import urllib.request as request
import ssl
import json

ssl._create_default_https_context = ssl._create_unverified_context

src = "https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json"
with request.urlopen(src) as response:
    data = json.load(response)

attractions = data["result"]["results"]
csv_file_path = "attractions.csv"
fieldnames = ["景點名稱", "區域", "經度", "緯度", "第一張圖檔網址"]
with open(csv_file_path, mode="w", encoding="utf-8", newline="") as csv_file:
    writer = csv.DictWriter(csv_file,fieldnames=fieldnames)
   
    for attraction in attractions:
        test = attraction["file"]
        start_index = test.index("http")
        end_index = test.lower().index(".jpg", start_index) + 4
        file_url = test[start_index:end_index]
        
        writer.writerow({
        "景點名稱": attraction["stitle"], 
        "區域": attraction["address"][5:8], 
        "經度": attraction["longitude"], 
        "緯度": attraction["latitude"], 
        "第一張圖檔網址": file_url
        })

print("CSV文件已成功生成：",csv_file_path)
