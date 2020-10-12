import csv

eb_csv = csv.DictReader(open("./local/20200912.csv"))

for row in eb_csv:
    if row.startswith(!"97"):
        return
    else:
        print(row)