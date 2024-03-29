# Задание 2.
# Создайте в переменной data список значений разных типов перечислив их через запятую внутри квадратных скобок.
# Для каждого элемента в цикле выведите:
# - порядковый номер;
# - значение;
# - адрес в памяти;
# - размер в памяти;
# - хэш объекта;
# - результат проверки на целое число только если он положительный;
# - результат проверки на строку только если он положительный.
# Добавьте в список повторяющиеся элементы и сравните на результаты

from os import sys

data = [42, 73.0, 'Hello world!', True, 42, 'Hello world!', 256, 2 ** 8, 1, 'Привет, мир!']

for i, elem in enumerate(data):
    print(f'#{i}: {elem} - {id(elem)} - {sys.getsizeof(elem)} - {hash(elem)} - {isinstance(elem, int)} - {isinstance(elem, str)}')
