"""
Напишите функцию, которая ищет json файлы в указанной директории
и сохраняет их содержимое в виде одноименных pickle файлов.
"""

import json
import pickle
import os


def json_to_pickle(directory):
    for file in os.listdir(directory):
        if file.endswith(".json"):
            with open(os.path.join(directory, file), "r") as f:
                data = json.load(f)
            with open(os.path.join(directory, file[:-5] + ".pickle"), "wb") as f:
                pickle.dump(data, f)


if __name__ == '__main__':
    json_to_pickle("C:\\Users\\max16\\PycharmProjects\\seminarGB\\venv\\python_again\\venv\\Seminar_8")
