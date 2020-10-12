# squarespace_csv = open('./local/products_Oct-13_10-11-40AM.csv', 'r')

# # print(squarespace_csv.readline())
# # print(squarespace_csv.readlines()[5:10])

# for title in squarespace_csv.readlines():
#     print(title)

# squarespace_csv.close()

squarespace_template = open('./local/products_template.csv', 'a')

squarespace_template.write('"5f6190cf6a1bfb1eec476d1c","479ba750-0052-4f46-9984-425fbcd5aece"\n')

squarespace_template.close()

from title_class import Title_sq

test_title = Title("5f6190dc6a1bfb1eec476e2b","a046c4d8-4424-4c11-a6d1-8f9f2a777992","PHYSICAL","shop-new","relentless-how-a-mother-and-daughter-defied-the-odds-lisa-tamati-9781925935998-book","Relentless","<h3 style=""white-space:pre-wrap;"">Lisa Tamati</h3>","9781925935998","","","","","","","35.00","0.00","No","3","/aotearoa/non-fiction","","0.0","0.0","0.0","0.0","Yes","https://static1.squarespace.com/static/5e8b986baae4b1034a683d73/5f6135f293ace752072f2660/5f6190dc6a1bfb1eec476e2c/1600229601312/9781925935998.jpg")

print(test_title.title)