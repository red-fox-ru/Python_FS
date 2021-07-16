# Name:        Оформление входящих чисел
# Author:      Panin Stanislav
# Created:     13.03.2021


list_word = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']


def search_int_try(ls):
    list_id = []
    for el in range(0, len(ls)):
        try:
            num = int(ls[el])
            if len(ls[el]) < 2:
                ls[el] = '0' + ls[el]
            if '+' in ls[el]:
                if len(str(num)) < 2:
                    ls[el] = int(ls[el])
                    ls[el] = '+0' + str(ls[el])
            list_id.append(el)
        except ValueError:
            ls[el] = ls[el] + ' '
    return list_id


def edited_list(lis, id_el):
    id_el.reverse()
    for el in id_el:
        lis.insert(el + 1, '" ')
        lis.insert(el, '"')
    lis = ''.join(str(i) for i in lis)
    return lis


def main():
    id_elm = search_int_try(list_word)
    print(edited_list(list_word, id_elm))


if __name__ == '__main__':
    main()
