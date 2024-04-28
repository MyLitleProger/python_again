"""
Напишите функцию, которая в бесконечном цикле запрашивает имя, личный идентификатор и уровень доступа (от 1 до 7).
После каждого ввода добавляйте новую информацию в JSON файл.
Пользователи группируются по уровню доступа.
Идентификатор пользователя выступает ключом для имени.
Убедитесь, что все идентификаторы уникальны независимо от уровня доступа.
При перезапуске функции уже записанные в файл данные должны сохраняться.
"""

from pathlib import Path
import json


def set_users(file: Path) -> None:
    u_ids = set()
    if not file.is_file():
        # data = {i: {} for i in range(1, 7 + 1)}
        data = {str(i): {} for i in range(1, 7 + 1)}
        # pass
    else:
        with open(file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        for value in data.values():
            u_ids.update(value.keys())

    while True:
        name = input('Введите имя: ')
        if not name:
            break
        u_id = input('Введите id: ')
        lvl = input('Введите уровень доступа: ')
        if ~ (u_id in u_ids and data[lvl].get(u_id) is None):
            data[lvl].update({u_id: name})
            with open(file, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)


if __name__ == '__main__':
    set_users(Path('users.json'))
