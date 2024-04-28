"""
Прочитайте созданный в прошлом задание csv файл без использования csv.DictReader.
Распечатайте его как pickle строку.
"""

import pickle
import csv
from pathlib import Path


def csv_to_pickle(file: Path) -> None:

    pickle_list = []
    with open(file, 'r', newline='', encoding='utf-8') as f:
        csv_file = csv.reader(f, dialect='excel-tab')
        for i, row in enumerate(csv_file):
            if i == 0:
                pickle_keys = row
            else:
                pickle_dict = dict(zip(pickle_keys, row))
                # pickle_dict = {k: v for k, v in zip(pickle_keys, row)}
                # print(pickle_dict)
                pickle_list.append(pickle_dict)
    print(pickle.dumps(pickle_list))


if __name__ == '__main__':
    csv_to_pickle(Path('data.csv'))