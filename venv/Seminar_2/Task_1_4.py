# Задание 4
# - Напишите программу, которая вычисляет площадь круга и длину окружности по введенному диаметру;
# - Диаметр не превышает 1000 у.е.;
# - Точность вычислений должна составлять не менее 42 знаков после запятой.

import math
import decimal


def circle_area(*args):
    """Возвращает площадь круга
    :param args: Диаметр
    :return: pi * r^2 - с точностью до 42 знаков"""
    radius: decimal.Decimal = decimal.Decimal(args[0] / 2)
    decimal.getcontext().prec = 42
    return decimal.Decimal(math.pi) * radius ** 2


def circle_perimeter(*args):
    """Возвращает периметр круга
    :param args: Диаметр
    :return: 2 * pi * r - с точностью до 42 знаков"""
    radius: decimal.Decimal = decimal.Decimal(args[0] / 2)
    decimal.getcontext().prec = 42
    return 2 * decimal.Decimal(math.pi) * radius


while True:
    try:
        diameter = int(input('Введите диаметр круга: '))
        break
    except ValueError:
        print('Введите целое число типа int')

print('Площадь круга: ', circle_area(diameter))
print('Длина окружности: ', circle_perimeter(diameter))
