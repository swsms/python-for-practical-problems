import xlrd

workbook = xlrd.open_workbook('module2_xlsx/lesson1/tab.xlsx')
sheet_names = workbook.sheet_names()

sh = workbook.sheet_by_name(sheet_names[0])
nmin = sh.row_values(6)[2]

for row_num in range(7, 27):
    temp = sh.row_values(row_num)
    nmin = min(nmin, temp[2])

print(nmin)
