"""
Напишите функцию, которая сохраняет созданный в прошлом задание файл в формате CSV.
"""

import csv
from pathlib import Path
import json


def json_to_csv(file: Path) -> None:

    with open(file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    list_rows = []
    for lvl, id_name_dict in data.items():
        for u_id, name in id_name_dict.items():
            list_rows.append({'level': int(lvl), 'id': int(u_id), 'name': name})

    with open(file.with_suffix('.csv'), 'w', encoding='utf-8') as f:
        csv_writer = csv.DictWriter(f, fieldnames=['level', 'id', 'name'], dialect='excel-tab')
        csv_writer.writeheader()
        csv_writer.writerows(list_rows)


if __name__ == '__main__':
    json_to_csv(Path('users.json'))
