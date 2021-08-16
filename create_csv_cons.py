# Name:        Чтение файла CSV через консоль с помощью параметров
# Author:      Panin Stanislav
# Created:     30.03.2021

import csv, sys


def sum_csv():
    with open('bakery.csv', 'r', encoding='utf-8') as f:
        rd = csv.reader(f)
        return sum([int(el[0]) for el in rd])


def all_value(start=False, ending=False):
    with open('bakery.csv', 'r', encoding='utf-8') as f:
        if start:
            for_arg_read = (el_sum for el_sum in csv.reader(f))
            try:
                for _ in range(start):
                    skip = next(for_arg_read)
            except TypeError:
                pass
            if ending:
                result = []
                try:
                    for _ in range(ending):
                        result.append(next(for_arg_read))
                except TypeError:
                    pass
                return result
            else:
                return [f'{item}, {idn}' for item, idn in for_arg_read]
        else:
            return [f'{el}, {idn}' for el, idn in (_ for _ in csv.reader(f))]


if __name__ == '__main__':
    param = sys.argv[1:]
    try:
        start, ends = int(param[0].replace(',','')), int(param[1])
    except IndexError:
        try:
            start, ends = int(param[0]), False
        except IndexError:
            start, ends = False, False
    output = all_value(start, ends)
    for el in output:
        print(el)
