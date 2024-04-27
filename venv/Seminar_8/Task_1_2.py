"""
Напишите функцию, которая в бесконечном цикле запрашивает имя, личный идентификатор и уровень доступа (от 1 до 7).
После каждого ввода добавляйте новую информацию в JSON файл.
Пользователи группируются по уровню доступа.
Идентификатор пользователя выступает ключом для имени.
Убедитесь, что все идентификаторы уникальны независимо от уровня доступа.
При перезапуске функции уже записанные в файл данные должны сохраняться.

Пример:

{
    "1": {
        "name": "John",
        "access_level": 1
    },
    "2": {
        "name": "Jane",
        "access_level": 2
    }
}
"""

from pathlib import Path
import json


def set_users(file: Path) -> None:
    if not file.exists():
        with open(file, 'w', encoding='utf-8') as f:
            json.dump({}, f)

    with open(file, 'r', encoding='utf-8') as f:
        users = json.load(f)

    while True:
        _name = input('Enter name: ')
        if _name == 'stop':
            break

        _id = input('Enter id: ')

        try:
            _access_level = int(input('Enter access level: '))
        except ValueError:
            print('Access level must be integer')
            continue

        if _id in users:
            print('This id is already taken')
            continue

        users[_id] = {'name': _name, 'access_level': _access_level}

        with open(file, 'w', encoding='utf-8') as f:
            json.dump(users, f)


if __name__ == '__main__':
    set_users(Path('users.json'))
