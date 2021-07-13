# Name:        Работа с ценами на товары
# Author:      Panin Stanislav
# Created:     13.03.2021

list_price = [17.91, 102.72, 88.06, 83.12, 12.28, 90.86, 84.5, 43.31, 16, 69.45, 95, 15.50,
              93.71, 124.74, 238, 76.44, 202.42, 799.30, 34.80, 85.05]


def view_price(ls_price):
    view_rub = [f'{int(el // 1)} руб' for el in ls_price]
    view_kop = []

    for el in ls_price:
        kopeks = int(round(((el % 1) * 100), 2))
        if kopeks != 0:
            if len(str(kopeks)) == 1:
                kopeks = f'{kopeks:02d} коп'
                view_kop.append(kopeks)
                continue
        else:
            kopeks = f'{kopeks:02d}'
        view_kop.append(f'{kopeks} коп')

    result = [f'{rub} {kop}' for rub, kop in zip(view_rub, view_kop)]

    return result


def main(ls_price):
    print(', '.join(str(i) for i in view_price(ls_price)))

    ls_price.sort()
    print(ls_price)
    print('id списка одинаков: ', id(ls_price) == id(list_price))

    price_reverse = ls_price.copy()
    price_reverse.sort(reverse=True)
    print(price_reverse)

    max_price = [ls_price.pop(ls_price.index(max(ls_price))) for _ in range(5)]
    max_price.sort()
    print(max_price)


if __name__ == '__main__':
    main(list_price)
