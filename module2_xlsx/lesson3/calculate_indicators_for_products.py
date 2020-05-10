from typing import Dict

import xlrd


def load_products_dict(sheet) -> Dict:
    values = [sheet.row_values(row_num) for row_num in range(sheet.nrows)]

    products_dict = dict()
    for row in values[1:]:
        product_name = str(row[0])
        row_values = [value if value != '' else '0' for value in row[1:]]
        values = list(map(float, row_values))
        products_dict[product_name] = values

    return products_dict


def load_products_by_weight_per_day(sheet) -> Dict:
    values = [sheet.row_values(row_num) for row_num in range(sheet.nrows)]

    products_by_weight = dict()
    for row in values[1:]:
        product_name = str(row[0])
        weight = int(row[1])
        if product_name not in products_by_weight:
            products_by_weight[product_name] = weight
        else:
            products_by_weight[product_name] += weight

    return products_by_weight


workbook = xlrd.open_workbook('module2_xlsx/lesson3/products_2.xlsx')
sheet_names = workbook.sheet_names()

products_sheet = workbook.sheet_by_name(sheet_names[0])
products_dict = load_products_dict(products_sheet)
# print(products_dict)

products_per_day_sheet = workbook.sheet_by_name(sheet_names[1])
products_by_weight = load_products_by_weight_per_day(products_per_day_sheet)
print(products_by_weight)

indicators = [0, 0, 0, 0]
for product_name, weight in products_by_weight.items():
    coefficient = weight / 100
    values = [value * coefficient for value in products_dict[product_name]]
    indicators = [x + y for x, y in zip(values, indicators)]

print(list(map(int, indicators)))
