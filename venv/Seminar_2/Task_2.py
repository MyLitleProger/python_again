# Задание 2.
# Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление. 
# Функцию hex используйте для проверки своего результата.


def convert_to(number, base, upper=False):
    digits = '0123456789abcdefghijklmnopqrstuvwxyz'
    if base > len(digits): return None
    result = ''
    while number > 0:
        result = digits[number % base] + result
        number //= base
    return result.upper() if upper else result

if __name__ == '__main__':
    while True:
        try:
            num = int(input('Введите целое число: '))
            break
        except ValueError:
            print('Введите целое число типа int')

    print('# user')
    print(convert_to(num, 16), '\n')
    print('# hex')
    print(hex(num), '\n')
    print('# format')
    print(format(num, 'x'))