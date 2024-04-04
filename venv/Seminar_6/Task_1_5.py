# Добавьте в модуль с загадками функцию, которая хранит словарь списков.
# Ключ словаря - загадка, значение - список с отгадками.
# Функция в цикле вызывает загадывающую функцию, чтобы передать ей все свои загадки.

from Task_1_4 import riddle


def storage():
    puzzles = {
        "Who was the first president of Russia?": ["Борис Николаевич Ельцин", "Boris Nikolaevich Yeltsin", "Ельцин", "Yeltsin"],
        "What is the name of the first dog in space?": ["Belka", "Белка", "Strelka", "Стрелка", "Laika", "Лайка"],
        "In what year was python developed?": ['1991'],
    }

    for puzzle, answer in puzzles.items():
        print(riddle(puzzle, answer))


if __name__ == '__main__':
    storage()
    