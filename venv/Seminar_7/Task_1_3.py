# Напишите функцию, которая открывает на чтение созданные
# в прошлых задачах файлы с числами и именами.
# Перемножьте пары чисел. В новый файл сохраните имя и произведение:
# если результат умножения отрицательный, сохраните его имя записанное строчными буквами и произведение по модулю
# если результат умножения положительный, сохраните имя прописными буквами и произведение округленные до целого.
# В результирующем файле должно быть столько же строкЮ сколько в более длинном файле.
# При достижении конца более короткого файла, возвращайтесь в его начало.

from pathlib import Path
from typing import TextIO


def begin(fd: TextIO) -> str:
    text = fd.readline()
    if text == '':
        fd.seek(0)
        text = fd.readline()
    return text.rstrip()


def convert_lines(names: Path, numbers: Path, result_file: Path) -> None:
    with (
        open(names, 'r', encoding='utf-8') as f_names, 
        open(numbers, 'r', encoding='utf-8') as f_numbers, 
        open(result_file, 'a', encoding='utf-8') as f_result
    ):
        len_names = sum(1 for _ in f_names)
        len_numbers = sum(1 for _ in f_numbers)
        max_len = max(len_numbers, len_names)
        for _ in range(max_len):
            name = begin(f_names)
            nums_str = begin(f_numbers)
            num_i, num_f = map(float, nums_str.split('|'))

            result = num_i * num_f
            if result < 0:
                f_result.write(name.lower() + ' ' + str(int(result)) + '\n')
            else:
                f_result.write(name.upper() + ' ' + str(int(result)) + '\n')

            print(name)
            print(nums_str)
            print(result)


if __name__ == '__main__':
    convert_lines(Path('names.txt'), Path('random_numbers.txt'), Path('result.txt'))
