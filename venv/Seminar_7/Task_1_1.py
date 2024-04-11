# Напишите функцию, которая заполняет файл
# (добавляет в конец) случайными парами чисел.
# Первое число int, второе - float разделены вертикальной чертой.
# Минимальное число - -1000, максимальное - +1000
# Количество строк и имя файла передаются как аргументы функции.

from random import randint, uniform
from pathlib import Path

MIN_NUMBER = -1000
MAX_NUMBER = 1000


def write_random_numbers(file_name: str, number_of_lines: int) -> None:
    with open(file_name, 'a', encoding='utf-8') as file:
        for _ in range(number_of_lines):
            file.write(f'{randint(MIN_NUMBER, MAX_NUMBER)}|{uniform(MIN_NUMBER, MAX_NUMBER)}\n')


if __name__ == '__main__':
    file_name = Path(__file__).parent / 'random_numbers.txt'
    write_random_numbers(file_name, 100)

