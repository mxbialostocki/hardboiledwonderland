import pandas as pd

read_file = pd.read_excel (r'./local/ebility_category_test.xls')

print(read_file)

read_file.to_csv (r'./local/generated/', index=None, header=True)