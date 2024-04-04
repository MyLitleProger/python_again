# Создайте модуль с функцией внутри.
# Функция получает на вход загадку, список с возможными вариантами отгадок и количество попыток на угадывание.
# Программа возвращает номер попытки, с которой была отгадана загадка или ноль, если попытки исчерпаны.


import random


def guess_the_number(question, answers, attempts):
    for i in range(attempts):
        print(f"{i + 1} attempt")
        print(question)
        answers = [i.lower() for i in answers]
        answer = input("Your answer: ")
        if answer.lower() in answers:
            print(f"You guessed the right answer on the {i + 1} attempt")
            return i + 1
    print("You ran out of attempts")
    return 0


if __name__ == "__main__":
    question = "What is the capital of Russia?"
    answers = ["Moscow", "Москва", "МСК", "MSC"]
    attempts = 3
    print(guess_the_number(question, answers, attempts))