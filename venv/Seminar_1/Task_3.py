# Напишите код, который запрашивает число и сообщает, является ли оно простым или составным.
# Используйте правило для проверки: “Число является простым, если делится нацело только на единицу и на себя”.
# Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.


# example 1
def is_prime(number):
    '''checking a number is prime or not
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
def test_is_prime():
    assert is_prime(1) == False
    assert is_prime(2) == True
    assert is_prime(3) == True
    assert is_prime(4) == False
    assert is_prime(5) == True
    assert is_prime(6) == False
    assert is_prime(7) == True
    assert is_prime(8) == False
    assert is_prime(9) == False
    assert is_prime(10) == False


test_is_prime()


# user testing
while True:
    try:
        number = int(input('Enter a number: '))
        if 0 < number < 100_000:
            break
        else:
            print('Write a numbers (0..100.000)')
    except ValueError:
        print('Write only numbers!')

if is_prime(number):
    print('This number is prime!')
else:
    print('This number is not prime!')
