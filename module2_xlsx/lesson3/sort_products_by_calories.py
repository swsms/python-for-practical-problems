import xlrd

workbook = xlrd.open_workbook('module2_xlsx/lesson3/products_1.xlsx')
sheet_names = workbook.sheet_names()

sheet = workbook.sheet_by_name(sheet_names[0])
values = [sheet.row_values(row_num) for row_num in range(sheet.nrows)]

product_and_calories_pairs = []

for row in values[1:]:
    product_and_calories_pairs.append((row[0], row[1]))

product_and_calories_pairs = sorted(product_and_calories_pairs,
                                    key=lambda pair: (-pair[1], pair[0]))

for pair in product_and_calories_pairs:
    print(pair[0])
