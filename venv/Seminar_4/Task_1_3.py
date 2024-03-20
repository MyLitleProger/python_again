# Функция получает на вход строку из двух чисел через пробел.
# Сформируйте словарь, где ключом будет символ из Unicode, а значением - целое число.
# Диапазон пар ключ-значение от наименьшего из введенных пользователем чисел до наибольшего включительно.


def range_unicode(text: str) -> dict[str, int]:
    first, second = text.split()
    first, second = int(first), int(second)
    return {chr(i): i for i in range(first, second + 1)}


print(range_unicode("10 15"))
