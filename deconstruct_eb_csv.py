import pandas as pd

eb_csv = pd.read_csv("./local/ebility_category_test_csv.csv", sep=',', names=None)

print(eb_csv[0:-1])
print(eb_csv.head())

# for i in eb_csv:
#     print(i)