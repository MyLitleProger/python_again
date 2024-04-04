# Создайте модуль с функцией внутри.
# Функция принимает на вход три целых числа: нижнюю и
# верхнюю границу и количество попыток.
# Внутри генерируется случайное число в указанных границах
# и пользователь должен угадать его за заданное число попыток
# функция выводит подсказки больше и меньше 
# если число угадано, возвращается истина, а если попытки исчерпаны - ложь

from random import randint


def guess_number(lower_bound=1, upper_bound=10, attempts=3):
    number = randint(lower_bound, upper_bound)
    for i in range(attempts):
        print(f"Try to guess the number from {lower_bound} to {upper_bound}")
        guess = int(input())
        if guess == number:
            print("You guessed it!")
            return True
        elif guess < number:
            print("Too small")
        else:
            print("Too big")
    print("You've run out of attempts")
    return False


if __name__ == "__main__":
    print(guess_number())
