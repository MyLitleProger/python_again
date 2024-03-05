# Напишите код, который запрашивает число и сообщает является ли оно простым или составным.
# Используйте правило для проверки: “Число является простым, если делится нацело только на единицу и на себя”.
# Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.

# example 1
def is_prime_1(number):
    '''cheking a number is prime or not
    :param number: number to check
    :return: True if number is prime, False if not
    '''
    if number == 1:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False
    for i in range(3, int(number ** 0.5) + 1, 2):
        if number % i == 0:
            return False
    return True

# testing example 1
def test_is_prime_1():
        assert is_prime_1(1) == False
        assert is_prime_1(2) == True
        assert is_prime_1(3) == True
        assert is_prime_1(4) == False
        assert is_prime_1(5) == True
        assert is_prime_1(6) == False
        assert is_prime_1(7) == True
        assert is_prime_1(8) == False
        assert is_prime_1(9) == False
        assert is_prime_1(10) ==False

# example 2
import math
def is_prime_2(num):
    '''cheking a number is prime or not with math module
    :param num: number to check
    :return: True if number is prime, False if not
    '''
    return math.is_prime(num)
# testing example 2
def test_is_prime_2():
    assert is_prime_2(1) == False
    assert is_prime_2(2) == True
    assert is_prime_2(3) == True
    assert is_prime_2(4) == False
    assert is_prime_2(5) == True
    assert is_prime_2(6) == False
    assert is_prime_2(7) == True
    assert is_prime_2(8) == False
    assert is_prime_2(9) == False
    assert is_prime_2(10) ==False
# user testing
while True:
    try:
        number = int(input('Enter a number: '))
        if 0 < number < 100_000:
            break
        else: print('Write a numbers (0..100.000)')
    except ValueError:
        print('Write only numbers!')


if is_prime_1(number):
    print('This number is prime!')
else:
    print('This number is not prime!')

if is_prime_2(number):
    print('This number is prime!')
else:
    print('This number is not prime!')