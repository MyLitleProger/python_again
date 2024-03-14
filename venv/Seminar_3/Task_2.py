# Дан список повторяющихся элементов.
# Вернуть список с дублирующимися элементами.
# В результирующем списке не должно быть дубликатов.

import random


def duplicate(arr):
    result = []
    for i in arr:
        if arr.count(i) > 1:
            result.append(i)
    return list(set(result))


arr = [random.randint(0, 10) for i in range(10)]
print(arr)
print(duplicate(arr))