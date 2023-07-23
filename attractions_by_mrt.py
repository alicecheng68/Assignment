import urllib.request as request
import ssl
import json
import csv

ssl._create_default_https_context = ssl._create_unverified_context

src = "https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json"
with request.urlopen(src) as response:
    data = json.load(response)  #data抓取src的資料

attractions = data["result"]["results"]   #抓取data裡的results資料
# key:mrt value:stitle
attractions_by_mrt = {}  

for attraction in attractions:  #attractions裡的每個項目叫attraction
    stitle = attraction["stitle"]  #attraction的stitle=stitle
    mrt = attraction["MRT"]

    if mrt in attractions_by_mrt:    #如果mrt已經在attraction_by_mrt裡，就加上stitle
        attractions_by_mrt[mrt].append(stitle)
    else:                           #如果沒有，加mrt和stitle
        attractions_by_mrt[mrt] = [stitle]

csv_file_path = "attractions_by_mrt.csv"


fieldnames = ["捷運站名稱", "景點"] #csv格式是捷運站,景點

with open(csv_file_path, mode="w", encoding="utf-8", newline="") as csv_file:
    writer = csv.writer(csv_file)  #寫入csv檔案
    

    for Mrt, Spots in attractions_by_mrt.items():  
        writer.writerow([Mrt if Mrt is not None else "無", *Spots])
    #改成用list的方式輸出結果，如果Mrt是空白的，則顯示“無”；如果用字串格式輸出，字典中有多個value時，前後會有雙引號
print("CSV文件已成功生成：", csv_file_path)

