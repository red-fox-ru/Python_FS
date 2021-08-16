# Name:        Сохранение логов и поиск IP адресса спамера
# Author:      Panin Stanislav
# Created:     29.03.2021


import requests, re, sys
from my_lib import get_element
from collections import Counter


def save_file(url):
    with open('logs.txt', 'w', encoding='utf-8') as f:
        obj = get_element(url)

        address = [el.split(' ')[0] for el in obj.split('\n')[0:]]
        address.pop()  # последний элемент address пустая строка

        request_type = re.findall(r'"[TCNSRDPOHEAGILU]+\s[^A-Za-z()]', obj)  # поиск регулярным выражением
        request_type = [el.replace(' /', '').replace('"', '') for el in request_type]  # удаляем ключевые символы поиска

        requested_resource = re.findall(r'/\w+/\w+[_]\w', obj)  # поиск регулярным выражением
        all_clients = list(zip(address, request_type, requested_resource))

        f.write(str(all_clients))
        return all_clients


def search_spammer(my_list: list, len_list):
    """
    Recursion binary search
    :param my_list:
    :param len_list:
    :return:
    """
    multi_req = [item for item in set(my_list) if my_list.count(item) > len_list]
    if len(multi_req) == 1:
        print(f'{multi_req[0]}: {len_list}')
        return True
    elif len(multi_req) > 1:
        search_spammer(my_list, int(len_list * 1.5))
    else:
        search_spammer(my_list, int(len_list / 2))


def search_spam_count(my_list):
    """
    Search max request
    :param my_list:
    :return:
    """
    spam = dict(Counter(my_list))
    item = 0
    result = ''
    for el in spam:
        if spam[el] > item:
            item = spam[el]
            result = f'{el}: {spam[el]}'
    return result


def main():
    all_clients = save_file(
        'https://raw.githubusercontent.com/elastic/examples/master/Common%20Data%20Formats/nginx_logs/nginx_logs')

    # первый вариант решения, recursion
    search_spammer(all_clients, len(all_clients))

    # второй вариант решения, модуль collections
    spammer = search_spam_count(all_clients)
    print(spammer)


if __name__ == '__main__':
    main()
