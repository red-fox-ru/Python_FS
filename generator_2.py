# Name:        Генератор кортежей
# Author:      Panin Stanislav
# Created:     25.03.2021

from itertools import zip_longest

TUTORS = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена'
]

CLASSES = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']


def main():
    # первый вариант решения - через генератор
    gen_haskel = (el for el in zip_longest(TUTORS, CLASSES))
    print(type(gen_haskel))
    for _ in range(0, len(CLASSES)):
        print(next(gen_haskel))

    # второй вариант решения
    comp_haskel = list(zip_longest(TUTORS, CLASSES))
    for el in comp_haskel:
        print(el)


if __name__ == '__main__':
    main()
