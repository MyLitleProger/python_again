# Дорабатываем функции из предыдущих задач.
# Генерируем файлы в указанную директорию - отдельный параметр функции.
# Отсутствие / наличие директории не должно вызывать ошибок в работе функции (добавьте проверки).
# Существующие файлы не должны удаляться изменяться в случае совпадения имен.

from random import randint, choices
from string import ascii_letters, digits
from os import choir
from pathlib import Path


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


def create_files_with_extensions(extensions, files_count):
    for extension in extensions:
        create_files(extension, files_count[extension])


create_files_with_extensions([".txt", ".py", ".jpg"], {".txt": 5, ".py": 3, ".jpg": 10})

