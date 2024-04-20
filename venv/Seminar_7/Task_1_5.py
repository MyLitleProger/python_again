# Создайте функцию которая генерирует файлы с разными расширениями
# Расширения и количество файлов функция принимает в качестве параметров
# Количество переданных расширений может быть любым
# Количество файлов для каждого расширения различно
# Внутри используйте вызов функции из прошколой задачи.

from Task_1_4 import create_files


def create_files_with_extensions(extensions, files_count):
    for extension in extensions:
        create_files(extension, files_count[extension])


create_files_with_extensions([".txt", ".py", ".jpg"], {".txt": 5, ".py": 3, ".jpg": 10})