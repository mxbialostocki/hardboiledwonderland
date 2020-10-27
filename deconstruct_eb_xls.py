import pandas as pd

df = pd.read_excel(open('/home/bxmbxm/workspace/hardboiledwonderland/local/ebility_category_test.XLS', 'r'))

print(df.readlines())

# df.to_csv (r'./local/generated/', index=None, header=True)