"""
Прочитайте созданный в прошлом задание csv файл без использования csv.DictReader.
Дополните id до 10 цифр незначащими нулями.
В именах первую букву сделайте прописной.
Добавьте хэш на основе имени и идентификатора.
Получившиеся записи сохраните в json файл, где каждая строка csv файла представлена как отдельный json словарь.
Имя исходного и конечного файлов передавайте как аргументы функции.
"""

from pathlib import Path
import json
import csv


def csv_to_json(csv_file: Path, json_file: Path) -> None:
    j_list = []
    with open(csv_file, 'r', encoding='utf-8', newline='') as f_csv:
        csv_reader = csv.reader(f_csv, dialect='excel-tab')
        for i, row in enumerate(csv_reader):
            json_dict = {}
            if i == 0 or not row:
                continue
            lvl, u_id, name = row
            json_dict['level'] = int(lvl)
            json_dict['id'] = f'{int(u_id):0>10}'
            json_dict['name'] = name.title()
            json_dict['hash'] = hash(f"{json_dict['name']}{json_dict['id']}")
            j_list.append(json_dict)

    with open(json_file, 'w', encoding='utf-8') as f_json:
        json.dump(j_list, f_json, indent=2, ensure_ascii=False)


if __name__ == '__main__':
    csv_to_json(Path('users.csv'), Path('data.json'))
