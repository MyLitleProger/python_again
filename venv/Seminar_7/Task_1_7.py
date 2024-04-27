# Создайте функцию для сортировки файлов по директориям: видео, изображение, текст и т.п.
# Каждая группа включает файлы с несколькими расширениями.
# В исходной папке должны остаться только те файлы, которые не подошли для сортировки.

from os import chdir
from pathlib import Path


def sort_files(path):
    chdir(path)
    for file in Path(path).iterdir():
        if file.is_file():
            if file.suffix in ('.mp4', '.avi', '.mkv'):
                file.rename(f'{file.parent}/video/{file.name}')
            elif file.suffix in ('.jpg', '.jpeg', '.png', '.gif'):
                file.rename(f'{file.parent}/image/{file.name}')
            elif file.suffix in ('.txt', '.doc', '.docx', '.pdf'):
                file.rename(f'{file.parent}/text/{file.name}')
            else:
                file.rename(f'{file.parent}/other/{file.name}')


if __name__ == '__main__':
    sort_files('C:\Users\max16\PycharmProjects\seminarGB\venv\python_again\venv\Seminar_7')
