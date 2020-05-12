import os
from typing import List, Set, Tuple

import xlrd
import xlwt

LESSON_PATH = 'module2_xlsx/lesson4'
COMPANY_DATA_PATH = f'{LESSON_PATH}/rogaikopyta'


def get_file_names(directory_name: str) -> Set[str]:
    file_names_in_dir = set()
    for (path, _, file_names) in os.walk(directory_name):
        for file_name in file_names:
            file_names_in_dir.add(file_name)
    return file_names_in_dir


def create_salary_xlsx(data_pairs: List[Tuple[str, int]]) -> None:
    salary_workbook = xlwt.Workbook()

    salary_sheet = salary_workbook.add_sheet('Salary list')
    salary_sheet.write(0, 0, 'Employee Name')
    salary_sheet.write(0, 1, 'Salary')

    current_row = 1
    for pair in data_pairs:
        salary_sheet.write(current_row, 0, pair[0])
        salary_sheet.write(current_row, 1, pair[1])
        current_row += 1

    salary_workbook.save(f'{LESSON_PATH}/salaries.xlsx')


employee_to_salary_dict = dict()
for file_path in get_file_names(COMPANY_DATA_PATH):
    workbook = xlrd.open_workbook(f'{COMPANY_DATA_PATH}/{file_path}')
    sheet_names = workbook.sheet_names()
    sheet = workbook.sheet_by_name(sheet_names[0])
    values = [sheet.row_values(row_num) for row_num in range(sheet.nrows)]
    name_salary_row = values[1]
    name = name_salary_row[1]
    salary = int(name_salary_row[3])

    if name in employee_to_salary_dict:
        salary = employee_to_salary_dict[name] + salary
    employee_to_salary_dict[name] = salary

employee_to_salary_pairs = list(employee_to_salary_dict.items())
employee_to_salary_pairs = sorted(employee_to_salary_pairs, key=lambda pair: pair[0])

for person, salary in employee_to_salary_pairs:
    print(f'{person} {salary}')

create_salary_xlsx(employee_to_salary_pairs)
