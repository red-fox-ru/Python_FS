# Name:        Переводчик чисел
# Author:      Panin Stanislav
# Created:     17.03.2021

from random import randint

global RUS_WORDS, ENG_WORDS

RUS_WORDS = ['Один', 'Два', 'Три', 'Четыре', 'Пять', 'Шесть', 'Семь', 'Восемь', 'Девять', 'Десять']
ENG_WORDS = ['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten']


def num_translate(word):
    word = word.lower()
    rus_eng = dict(zip(
        [el.lower() for el in RUS_WORDS],
        [el.lower() for el in ENG_WORDS]
    ))
    result = rus_eng.get(word)
    return result


def num_translate_adv(word):
    rus_eng_title = dict(zip(RUS_WORDS, ENG_WORDS))
    rus_eng_lower = dict(zip(
        [el.lower() for el in RUS_WORDS],
        [el.lower() for el in ENG_WORDS]
    ))
    if word.istitle():
        result = rus_eng_title.get(word)
    else:
        result = rus_eng_lower.get(word)
    return result


def main():
    ex_input = ['Один', 'два', 'три', 'Ноль', 'Пять', 'сорок', 'семь', 'восемь', 'Девять', 'десять']
    print('\nПервая функция, только перевод:')
    for el in range(0, 5):
        print(num_translate(ex_input[randint(0, 9)]))
    print(' \nВторая функция, реагирует на регистр:')
    for el in range(0, 5):
        print(num_translate_adv(ex_input[randint(0, 9)]))


if __name__ == '__main__':
    main()
