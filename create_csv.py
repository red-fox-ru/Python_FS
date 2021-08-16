# Name:        Запись CSV-файла через параметр
# Author:      Panin Stanislav
# Created:     30.03.2021

import csv, sys


def data_csv(data, id_num):
    with open('bakery.csv', 'a', encoding='utf8', newline='') as f:
        wr = csv.writer(f)
        wr.writerow([data['sum_sale'], id_num['ID']])


def main(chars):
    char, auth = chars
    value = {'sum_sale': char.replace(',', '')}
    create_num = {'ID': auth}
    data_csv(value, create_num)


if __name__ == '__main__':
    value = sys.argv[1:]
    main(value)
