import os
from typing import Set

import xlrd

BASE_PATH = 'module2_xlsx/lesson4/rogaikopyta'


def get_file_names(directory_name: str) -> Set[str]:
    file_names_in_dir = set()
    for (path, _, file_names) in os.walk(directory_name):
        for file_name in file_names:
            file_names_in_dir.add(file_name)
    return file_names_in_dir


person_to_salary_dict = dict()
for file_path in get_file_names(BASE_PATH):
    workbook = xlrd.open_workbook(f'{BASE_PATH}/{file_path}')
    sheet_names = workbook.sheet_names()
    sheet = workbook.sheet_by_name(sheet_names[0])
    values = [sheet.row_values(row_num) for row_num in range(sheet.nrows)]
    name_salary_row = values[1]
    name = name_salary_row[1]
    salary = int(name_salary_row[3])

    if name in person_to_salary_dict:
        salary = person_to_salary_dict[name] + salary
    person_to_salary_dict[name] = salary

person_to_salary_pairs = list(person_to_salary_dict.items())
person_to_salary_pairs = sorted(person_to_salary_pairs, key=lambda pair: pair[0])

for person, salary in person_to_salary_pairs:
    print(f'{person} {salary}')
