# Name:        Collection my funcs
# Author:      Panin Stanislav

import requests


def get_element(url):
    """
    Just GET-request
    :param url:
    :return:
    """
    r = requests.get(url)
    r.encoding = 'windows-1251'
    result = r.content.decode(encoding=r.encoding)
    return result


if __name__ == '__main__':
    print(get_element('https://www.google.ru/'))
