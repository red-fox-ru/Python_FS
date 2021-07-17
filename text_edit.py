# Name:        Стандартизация входящего текста
# Author:      Panin Stanislav
# Created:     13.03.2021

cooperators = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА',
               'токарь высшего разряда нИКОЛАЙ', 'директор авелина']


def key_name(ls_coop):
    ls_coop = [el.split()[-1].title() for el in ls_coop]
    for name in ls_coop:
        print(f'Привет, {name}!')


def main():
    key_name(cooperators)


if __name__ == '__main__':
    main()
