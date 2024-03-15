# Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения.
# Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность.
# Достаточно вернуть один допустимый вариант.
# *Верните все возможные варианты комплектации рюкзака.


def backpack(max_weight: int, items: dict[str, int]):
    item, weight = zip(*sorted(items.items(), key=lambda x: x[1], reverse=True))
    result, _temp_i, _temp_w = [], [], 0

    for i, w in enumerate(weight, 0):
        _temp_w += w
        _temp_i.append(item[i])

        for j, k in enumerate(weight[i:], i):
            if _temp_w + k <= max_weight:
                _temp_w += k
                _temp_i.append(item[j])

        result.append(_temp_i)
        _temp_i, _temp_w = [], 0

    return result


things = {'water': 1, 'food': 5, 'first aid kit': 2,
          'tent': 5, 'knife': 1, 'map': 1, 'compass': 1,
          'sleeping bag': 5, 'matches': 1, 'lighter': 1, 'tool kit': 3}

print(backpack(15, things))