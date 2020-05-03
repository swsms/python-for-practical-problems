from statistics import mean, median

import xlrd

workbook = xlrd.open_workbook('module2_xlsx/lesson2/salaries.xlsx')
sheet_names = workbook.sheet_names()

sheet = workbook.sheet_by_name(sheet_names[0])
values = [sheet.row_values(row_num) for row_num in range(sheet.nrows)]

jobs = [job for job in values[0] if job]  # jobs = values[0][1:]
regions = [row[0] for row in values if row[0]]

salaries_table = []
for row in values[1:]:
    salaries_table.append(row[1:])

median_salaries_by_regions = []
for salary_row in salaries_table:
    median_for_region = median(salary_row)
    median_salaries_by_regions.append(median_for_region)

max_median_value = max(median_salaries_by_regions)
max_median_index = median_salaries_by_regions.index(max_median_value)

print(regions[max_median_index])

mean_salaries_by_jobs = []
for i in range(7):
    average = mean([row[i] for row in salaries_table])
    mean_salaries_by_jobs.append(average)

max_mean_value = max(mean_salaries_by_jobs)
max_mean_index = mean_salaries_by_jobs.index(max_mean_value)

print(jobs[max_mean_index])
