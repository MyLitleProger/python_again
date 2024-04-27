"""
Напишите функцию, которая сохраняет созданный в прошлом задание файл в формате CSV.
"""

import csv
from pathlib import Path
import json


def save_csv(file: Path) -> None:
    """
    Конвертирует json в csv путем перезаписи данных.
    :param file:
    :return:
    """
    # Stop if file does not exist
    if not file.exists():
        return

    # Load json data
    with open(file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Convert data to list of dicts
    list_rows = []
    for key, value in data.items():
        for user in value:
            list_rows.append({'id': key, 'level': user[1], 'name': user[2]})

    # Save data as csv
    with open(f'{file.stem}.csv', 'w', newline='', encoding='utf-8') as f:
        csv_writer = csv.DictWriter(f, fieldnames=['level', 'id', 'name'], delimiter=';')
        csv_writer.writeheader()
        csv_writer.writerows(list_rows)


if __name__ == '__main__':
    save_csv(Path('users.json'))