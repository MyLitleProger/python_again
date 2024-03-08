# Задание 5.
# - Напишите программу, которая решает квадратные уравнения даже если дискриминант отрицательный;
# - Используйте комплексные числа для квадратного корня.

def solve_quadratic(*args: int):
    """Решает квадратные уравнения даже если дискриминант отрицательный
    :param args: 3 числа (a, b, c)
    :return: x1, x2 - корни уравнения, x - если a = 0"""
    a, b, c = args
    if a == 0:
        return -c / b
    else:
        delta = b ** 2 - 4 * a * c
        if delta < 0:
            delta = complex(delta, 0)
            x1 = (-b + delta ** .5) / (2 * a)
            x2 = (-b - delta ** .5) / (2 * a)
            return round(x1.real, 2) + round(x1.imag, 2) * 1j, round(x2.real, 2) + round(x2.imag, 2) * 1j
        elif delta == 0:
            x1 = x2 = -b / (2 * a)
            return x1, x2
        else:
            x1 = (-b + delta ** .5) / (2 * a)
            x2 = (-b - delta ** .5) / (2 * a)
            return x1, x2


while True:
    try:
        a = int(input('Введите число a: '))
        b = int(input('Введите число b: '))
        c = int(input('Введите число c: '))
        break
    except ValueError:
        print('Введите число типа int')

print(solve_quadratic(a, b, c))
