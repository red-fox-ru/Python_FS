# Name:        Поиск повторояющихся элементов
# Author:      Panin Stanislav
# Created:     25.03.2021

SRC = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]


def no_repeat_gen(ls):
    mass_dub = sorted(set([item for item in set(ls) if not ls.count(item) > 1]), key=ls.index)
    return mass_dub


def func_no_repeat(my_list):
    mass_dub = set()
    for el in set(my_list):
        if my_list.count(el) > 1:
            mass_dub.add(el)
    mass = set(my_list)
    return sorted(mass - mass_dub, key=my_list.index)


if __name__ == '__main__':
    print(no_repeat_gen(SRC))
    print(func_no_repeat(SRC))
