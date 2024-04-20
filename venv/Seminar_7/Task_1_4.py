# Создайте функцию, которая создает файлы с указанным расширением.
# Функция принимает следующие параметры:
# расширение
# минимальная длина случайно сгенерированного имени, по умолчанию 6
# максимальное длина случайно сгенерированного имени, по умолчанию 30
# минимальное число случайных байт, записанных в файл, по умолчанию 256
# максимальное число случайных байт, записанных в файл, по умолчанию 4096
# количество файлов, по умолчанию 42
# Имя файла и его размер должны быть в рамках переданного диапазона

from random import randint, choices
from string import ascii_letters, digits


def create_files(extension,
                 min_name_length=6,
                 max_name_length=30,
                 min_file_size=256,
                 max_file_size=4096,
                 number_of_files=42):

    for _ in range(number_of_files):
        file_name = ''.join(choices(ascii_letters + digits, k=randint(min_name_length, max_name_length)))
        file_size = randint(min_file_size, max_file_size)
        with open(f'{file_name}.{extension}', 'wb') as file:
            file.write(bytes(randint(0, 255) for _ in range(file_size)))


create_files('txt')
