# Вспомните задачу 3 из прошлого семинара. Мы сформированли текстовый файл с псевдо именами и произведением чисел.
# Напишите функцию, которая создает из созданного ранее файла новый с данными в формате JSON.
# Имена пишите с большой буквы.
# Каждую пару сохраняйте с новой строки.

import json
from pathlib import Path


def convert(file: str | Path) -> None:
    with open(file, 'r', encoding='utf-8') as f:
        data = f.readlines()
    data = [i.strip() for i in data]
    data = [i.split(' ') for i in data]
    data = {i[0].capitalize(): int(i[1]) for i in data}
    with open(file, 'w') as f:
        json.dump(data, f)


if __name__ == '__main__':
    convert('C:\\Users\\max16\\PycharmProjects\\seminarGB\\venv\\python_again\\venv\\Seminar_7\\result.txt')
