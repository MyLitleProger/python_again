# Написать программу определающую высокосный год или нет

while True:
    try:
        year = int(input('Введите год: '))
        if year:break
    except ValueError:
        print('Вводить нужно только числа в формате YYYY')


if year % 4 != 0 or year % 100 == 0 and year % 400 != 0:
    print('Обычный')
else: print('Високосный')