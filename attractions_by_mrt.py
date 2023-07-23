import urllib.request as request
import ssl
import json
import csv

ssl._create_default_https_context = ssl._create_unverified_context

src = "https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json"
with request.urlopen(src) as response:
    data = json.load(response)

attractions = data["result"]["results"]
# key:mrt value:spots
attractions_by_mrt = {}

for attraction in attractions:
    stitle = attraction["stitle"]
    mrt = attraction["MRT"]

    if mrt in attractions_by_mrt:
        attractions_by_mrt[mrt].append(stitle)
    else:
        attractions_by_mrt[mrt] = [stitle]


csv_file_path = "attractions_by_mrt.csv"


fieldnames = ["捷運站名稱", "景點"]

with open(csv_file_path, mode="w", encoding="utf-8", newline="") as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    

    for Mrt, Spots in attractions_by_mrt.items():
        Spots = ", ".join(Spots)
        writer.writerow({
            "捷運站名稱": Mrt 
            if mrt is not None else "Unknown", 
            "景點": Spots})

print("CSV文件已成功生成：", csv_file_path)
