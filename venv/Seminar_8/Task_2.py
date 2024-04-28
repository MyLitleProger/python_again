"""
Напишите функцию, которая получает на вход директорию и рекурсивно обходит её и все вложенные директории.
Результаты обхода сохраните в файлы json, scv и pickle.
Для дочерних объектов указывайте родительскую директорию.
Для каждого объекта укажите файл это или директория.
Для файлов сохраните его размер в байтах,
а для директорий размер файлов в ней с учетом всех вложенных файлов и директорий.
"""

import os
import json
import pickle
import csv


def get_info(path: str) -> dict:
    info = {}
    for item in os.listdir(path):
        item = os.path.join(path, item)
        if os.path.isfile(item):
            info[item] = {
                'type': 'file',
                'size': os.path.getsize(item)
            }
        elif os.path.isdir(item):
            info[item] = {
                'type': 'dir',
                'size': get_size(item)
            }
    save_json(path + '.json', info)
    save_csv(path + '.csv', info)
    save_pickle(path + '.pickle', info)
    return info


def save_json(path: str, info: dict):
    with open(path, 'w') as file:
        json.dump(info, file)


def save_csv(path: str, info: dict):
    with open(path, 'w') as file:
        writer = csv.writer(file)
        writer.writerow(['path', 'type', 'size'])
        for key, value in info.items():
            writer.writerow([key, value['type'], value['size']])


def save_pickle(path: str, info: dict):
    with open(path, 'wb') as file:
        pickle.dump(info, file)


if __name__ == '__main__':
    print(get_info("C:\\Users\\max16\\PycharmProjects\\seminarGB\\venv\\python_again\\venv\\Seminar_8"))
