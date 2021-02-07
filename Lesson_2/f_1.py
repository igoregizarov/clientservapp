import re
import csv

main_data = [['Изготовитель системы', 'Название ОС', 'Код продукта', 'Тип системы']]
os_prod_list = []
os_name_list = []
os_code_list = []
os_type_list = []


def search(text_search, row, list):
    text = re.compile(text_search)
    if len(text.findall(row)) > 0:
        res = re.sub(" +", "", row)
        res = res.split(':')
        # print(res[1])
        res = re.findall('.+', res[1])
        res = str(res[0])
        list.append(res)


def get_data(file):
    with open(file) as f:
        for line in f:
            search('Изготовитель системы', line, os_prod_list)
            search('Название ОС', line, os_name_list)
            search('Код продукта', line, os_code_list)
            search('Тип системы', line, os_type_list)


get_data('Студентам для решения домашнего задания\info_1.txt')
get_data('Студентам для решения домашнего задания\info_2.txt')
get_data('Студентам для решения домашнего задания\info_3.txt')

for num in range(len(os_prod_list)):
    lst = []
    lst.append(os_prod_list[num])
    lst.append(os_name_list[num])
    lst.append(os_code_list[num])
    lst.append(os_type_list[num])
    main_data.append(lst)


def write_to_csv(file):
    with open(file, 'w') as f:
        f_writer = csv.writer(f)
        for row in main_data:
            f_writer.writerow(row)

    with open(file) as f:
        print(f.read())


write_to_csv('less1.csv')
