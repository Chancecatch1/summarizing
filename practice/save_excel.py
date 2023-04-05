import csv

filename = "canada.csv"
f = open(filename, "w", encoding="utf-8-sig", newline="")
writer = csv.writer(f)

columns_title = ["Quebec", "Alberta"]
writer.writerow(columns_title)

data = ["Dawn", "Pine"] # [] 리스트 자료구조
writer.writerow(data)