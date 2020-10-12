# squarespace_csv = open('./local/products_Oct-13_10-11-40AM.csv', 'r')

# # print(squarespace_csv.readline())
# # print(squarespace_csv.readlines()[5:10])

# for title in squarespace_csv.readlines():
#     print(title)

# squarespace_csv.close()

squarespace_template = open('./local/products_template.csv', 'a')

squarespace_template.write('"5f6190cf6a1bfb1eec476d1c","479ba750-0052-4f46-9984-425fbcd5aece"\n')

squarespace_template.close()