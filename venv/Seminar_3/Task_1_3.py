# Создайте вручную кортеж содержащий элементы разных типов.
# Получите из него словарь списков, где:
# ключ - тип элемента,
# значение - список элементов данного типа.

data = 42, 1.23, 'hello', [1, 2, 3], {1, 2, 3}

result = {}
for i in data:
    if type(i) not in result:
        result[type(i)] = []
    result[type(i)].append(i)

print(result)
