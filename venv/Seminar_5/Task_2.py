# Напишите функцию, которая принимает на вход строку - абсолютный путь до файла.
# Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.

def get_path(path):
    _path = path.split('/')
    _file = _path[-1]
    name, extension = _file.split('.')
    _path = '/'.join(_path[:-1])
    return _path, name, extension


print(*get_path('/home/user/file.txt'))