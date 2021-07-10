# Name:        Работа со списками
# Author:      Панин Станислав
# Created:     11.03.2021


odd_cube= [i**3 for i in range(1, 1000) if i % 2 != 0]


def sum_num(number):
    summa = 0
    while number > 0:
        digit = number % 10
        summa += digit
        number //= 10
    return summa


def sample_sum_num(list_num, number):
    result = []
    for num in list_num:
        value = sum_num(num)
        if value % number == 0:
            result.append(num)
    return result


def main(first_list):
    print('Список состоящий из кубов нечётных чисел:')
    print(first_list)
    res_list = sample_sum_num(first_list, 7)
    print('Список из сумм цифр которых делится на 7 без остатка: ')
    print(res_list)
    print('Сумма чисел из списка: ')
    print(sum(res_list), '\n')
    for el in range(0, len(first_list)):
        first_list[el] += 17
    print('Каждому элементу списка прибавили 17: ')
    print(first_list)
    first_list = sample_sum_num(first_list, 7)
    print('Список из сумм цифр которых делится на 7 без остатка: ')
    print(first_list)
    print('Сумм чисел из списка: ')
    print(sum(first_list))


if __name__ == '__main__':
    main(odd_cube)
