# Name:        Элементы, значения которых больше предыдущего
# Author:      Panin Stanislav
# Created:     25.03.2021

from timeit import timeit
from sys import getsizeof

SRC = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]


def func_el(data):
    result = []
    for i in range(1, len(data)):
        if data[i] > data[i - 1]:
            result.append(data[i])
    return result


def time_code(operation):
    """
    Time work func
    :param operation:
    :return:
    """
    timer = timeit(f"""{operation}""")
    print(f'Время выполнения: {timer}')


def main():
    # первый вариант
    res_func = func_el(SRC)
    time_code(res_func)
    print('Объём памяти:', getsizeof(res_func))
    print(res_func)

    # второй вариант
    ls_val_a = SRC.copy()
    comp_haske = [ls_val_a[i] for i in range(1, len(ls_val_a)) if ls_val_a[i] > ls_val_a[i - 1]]
    time_code(comp_haske)
    print('Объём памяти:', getsizeof(comp_haske))
    print(comp_haske)

    # третий вариант
    ls_val_b = SRC.copy()
    zip_haske = [el for i, el in zip(ls_val_b, ls_val_b[1:]) if el > i]
    time_code(zip_haske)
    print('Объём памяти:', getsizeof(zip_haske))
    print(zip_haske)


if __name__ == '__main__':
    main()