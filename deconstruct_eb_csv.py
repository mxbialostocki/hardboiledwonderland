import pandas as pd

eb_csv = pd.read_csv("./local/ebility_category_test_csv.csv", sep=',', names=None, usecols=['ISBN','TITLE','ON HAND'])


# print(eb_csv[["isbn","title","qty sold","cost of sales","nett sales","rrp","on hand","profit"]])
# print(eb_csv.head())

web_titles = []

print(eb_csv.info())

# for el in eb_csv[3:13]:
#     print(el)
extraction = eb_csv[(len(eb_csv['TITLE']) > 15) & (eb_csv['ON HAND'] >= 30)]
print(extraction)

result = eb_csv.to_dict(orient='records')

for title in result:
    print(title["TITLE"], ' || ', title["ISBN"])

# for i in eb_csv:
#     print(i)