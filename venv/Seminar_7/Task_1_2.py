# Напишите функцию, которая генерирует псевдоимена.
# Имя должно начинаться с заглавной буквы,
# состоять из 4-7 букв, среди которых
# обязательно должны быть гласные.
# Полученные имена сохраните в файл.

from random import randint, choice
from pathlib import Path

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
MIN_LENGTH = 4
MAX_LENGTH = 7


def generate_name():
    name = ''
    while len(name) < MIN_LENGTH:
        name += choice(VOWELS)
    while len(name) < MAX_LENGTH:
        name += choice(CONSONANTS)
    return name.capitalize()


def main():
    names = [generate_name() for _ in range(100)]
    with open(Path(__file__).parent / 'names.txt', 'w') as f:
        f.write('\n'.join(names))


if __name__ == '__main__':
    main()