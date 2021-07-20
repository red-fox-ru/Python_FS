# Name:        Генератор шуток
# Author:      Panin Stanislav
# Created:     17.03.2021

from random import randint, shuffle


def get_jokes(value, repeat_word=True):
    """
    List-based joke generator

    :param value - number of jokes:
    :param repeat_word - True or False:
    :return:
    """
    result = []
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

    for _ in range(0, value):
        shuffle(nouns)
        shuffle(adverbs)
        shuffle(adjectives)
        if repeat_word:
            rofl = f'{nouns[1]} {adverbs[1]} {adjectives[1]}'
        else:
            try:
                rofl = f'{nouns.pop()} {adverbs.pop()} {adjectives.pop()}'
            except IndexError:
                rofl = 'Прости, шутки кончились...'

        result.append(rofl)
    return result


if __name__ == '__main__':
    print(get_jokes(6))
