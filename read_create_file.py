# Name:        Чтение и запись файлов
# Author:      Panin Stanislav
# Created:     29.03.2021

import csv, sys
from itertools import zip_longest


def read_csv(file):
    with open(file, 'r', encoding='utf-8') as f:
        return [" ".join(el) for el in csv.reader(f)]


def write_csv(file, data):
    with open(file, 'a', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(f'{el} : {data[el]}' for el in data)


def write_txt(file, data):
    with open(file, 'a', encoding='utf-8') as f:
        f.writelines(f'{el}: {data[el]}\n' for el in data)


def main(*args):
    f_1, f_2, result_file = args

    users = read_csv(f_1)
    hobby = read_csv(f_2)
    dict_usr = dict(zip_longest(users, hobby))
    try:
        if dict_usr[None]:
            sys.exit(1)
    except KeyError:
        print(dict_usr)
        write_txt(result_file, dict_usr)


if __name__ == '__main__':
    try:
        files = sys.argv[1:]
        main(files)
    except ValueError:
        main('users.csv', 'hobby.csv', 'user_hobby.txt')
