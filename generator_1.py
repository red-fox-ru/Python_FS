# Name:        Два вида генератора
# Author:      Panin Stanislav
# Created:     25.03.2021

LAST_NUM = 15


def odd_nums(num):
    for el in range(1, num + 1):
        if el % 2:
            yield el


def task_one():
    odd_to_15 = odd_nums(LAST_NUM)
    print(next(odd_to_15))
    print(next(odd_to_15), '\n')


if __name__ == '__main__':
    task_one()
    odd_to_15 = (el for el in range(1, LAST_NUM + 1) if el % 2)
    print(next(odd_to_15))
    print(next(odd_to_15))
