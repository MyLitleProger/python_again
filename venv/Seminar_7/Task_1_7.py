# Создайте функцию для сортировки файлов по директориям: видео, изображение, текст и т.п.
# Каждая группа включает файлы с несколькими расширениями.
# В исходной папке должны остаться только те файлы, которые не подошли для сортировки.

import os


def sort_files(path):
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith('.mp4') or file.endswith('.mkv'):
                os.rename(os.path.join(root, file), os.path.join(root, 'video', file))
            elif file.endswith('.jpg') or file.endswith('.png'):
                os.rename(os.path.join(root, file), os.path.join(root, 'image', file))
            elif file.endswith('.txt') or file.endswith('.doc') or file.endswith('.docx'):
                os.rename(os.path.join(root, file), os.path.join(root, 'text', file))
            else:
                os.rename(os.path.join(root, file), os.path.join(root, 'other', file))


# sort_files('C:\\Users\\User\\Desktop\\Seminar_7\\Task_1_7')
