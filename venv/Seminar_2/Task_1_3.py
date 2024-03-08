# Задание 3
# - Напишите программу, которая получает целое число и возвращает
# его двоичное, восьмеричное строковое представление.
# - Функции bin и oct используйте для проверки своего результата, а не для решения.
# Дополнительно:
# - Попробуйте избежать дублирования кода в преобразованиях к различным системам счисления;
# - Избегайте магических чисел;
# - Добавьте аннотацию типов, где это возможно.

while True:
    try:
        num = int(input('Введите целое число: '))
        break
    except ValueError:
        print('Введите целое число типа int')


def n_bin(*args):
    """
    Преобразует число в двоичный код
    :param args: Число типа int
    :return: Двоичный код
    """
    result: str = ''
    _num: int = args[0]
    while _num > 0:
        result = str(_num % 2) + result
        _num //= 2
    return result


def n_oct(*args):
    """
    Преобразует число в восьмеричный код
    :param args: Число типа int
    :return: Восьмеричный код
    """
    result: str = ''
    _num: int = args[0]
    while _num > 0:
        result = str(_num % 8) + result
        _num //= 8
    return result


print('# user')
print(f'Двоичное представление: {n_bin(num)}')
print(f'Восьмеричное представление: {n_oct(num)}\n')

print('# bin')
print(f'Двоичное представление: {bin(num)}')
print(f'Восьмеричное представление: {oct(num)}\n')

print('# format')
print(f'Двоичное представление: {format(num, "b")}')
print(f'Восьмеричное представление: {format(num, "o")}\n')
