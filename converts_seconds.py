# Name:        Конвертер секунд
# Author:      Red-F0X
# Created:     10.03.2021


FULL_STEP_CLOCK = 60
DAY_SEC = 86400
HOUR_SEC = 3600
MONTH_SEC = 2592000


def conversion(seconds):
    month = seconds // MONTH_SEC
    days = (seconds // DAY_SEC) % 31
    hour = (seconds // HOUR_SEC) % 24
    mint = (seconds // FULL_STEP_CLOCK) % FULL_STEP_CLOCK
    sec = seconds % FULL_STEP_CLOCK
    return month, days, hour, mint, sec


def main():
    try:
        duration = int(input('Введите число секунд: '))
    except ValueError:
        duration = int(input('Введите число цифрами от 0: '))

    month, days, hour, mint, sec = conversion(duration)

    if duration < 0:
        print('Число меньше нуля')
    elif duration < 60:
        print(f'{sec} сек')
    elif duration < HOUR_SEC:
        print(f'{mint} мин, {sec} сек')
    elif duration < DAY_SEC:
        print(f'{hour} час, {mint} мин, {sec} сек')
    elif duration < MONTH_SEC:
        print(f'{days} дн, {hour} час, {mint} мин, {sec} сек')
    elif duration >= MONTH_SEC:
        print(f'{month} м, {days} дн, {hour} час, {mint} мин, {sec} сек')


if __name__ == '__main__':
    main()
