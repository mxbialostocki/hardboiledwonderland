import pandas as pd

eb_csv = pd.read_csv("./local/ebility_category_test_csv.csv", sep=',', names=None, usecols=['ISBN','TITLE','ON HAND'])


# print(eb_csv[["isbn","title","qty sold","cost of sales","nett sales","rrp","on hand","profit"]])
# print(eb_csv.head())

web_titles = []

print(eb_csv.info())

# for el in eb_csv[3:13]:
#     print(el)

result = eb_csv.to_dict(orient='records')

print(result)
# for i in eb_csv:
#     print(i)