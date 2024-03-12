# Задание 3.
# Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем.
# Программа должна возвращать сумму и произведение* дробей. Для проверки своего кода используйте модуль fractions.


import fractions


def fraction():
    while True:
        try:
            a = input('Введите число а: ')
            b = input('Введите число b: ')
            if b == '0' or not b.isdigit() or not a.isdigit():
                print('a должно быть числом типа int\nb должно быть числом типа int отличным от 0')
                continue
            elif a[0] == '0' or b[0] == '0':
                print('числа не должны начинаться с 0')
                continue
            ab = a + '/' + b
            break
        except ValueError:
            print('Введите целое число типа int')
    return ab


def prime(n):
    i = 2
    prim = []
    while i * i <= n:
        while n % i == 0:
            prim.append(i)
            n = n / i
        i = i + 1
    if n > 1:
        prim.append(n)
    return prim


def nod(a, b):
    prime_a = prime(a)
    prime_b = prime(b)
    try:
        return max(set(prime_a).intersection(set(prime_b)))
    except ValueError:
        return 1


def sum_fractions(ab1, ab2):
    a1, b1 = map(int, ab1.split('/'))
    a2, b2 = map(int, ab2.split('/'))
    if b1 == b2:
        a = a1 + a2
        b = b1
        if a % b == 0:
            return a // b
        else:
            _temp = nod(a, b)
            a = a // _temp
            b = b // _temp
    else:
        a = a1 * b2 + a2 * b1
        b = b1 * b2
        if a % b == 0:
            return a // b
        else:
            _temp = nod(a, b)
            a = a // _temp
            b = b // _temp
    return str(a) + '/' + str(b)


def mul_fractions(ab1, ab2):
    a1, b1 = map(int, ab1.split('/'))
    a2, b2 = map(int, ab2.split('/'))
    a = a1 * a2
    b = b1 * b2
    if a % b == 0:
        return a // b
    if a != b:
        _temp = nod(a, b)
        a = a // _temp
        b = b // _temp
    return str(a) + '/' + str(b)


if __name__ == '__main__':
    print('Введите две дроби')
    fraction_1 = fraction()
    print(fraction_1)
    fraction_2 = fraction()
    print(fraction_2)

    print('-' * 20)
    print('# fractions')
    print('Сумма: ', fractions.Fraction(fraction_1) + fractions.Fraction(fraction_2))
    print('Произведение: ', fractions.Fraction(fraction_1) * fractions.Fraction(fraction_2))
    print('-' * 20)
    print('# user')
    print('Сумма: ', sum_fractions(fraction_1, fraction_2))
    print('Произведение: ', mul_fractions(fraction_1, fraction_2))
