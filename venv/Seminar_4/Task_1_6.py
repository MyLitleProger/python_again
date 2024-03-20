# Функция получает на вход список чисел и два индекса.
# Вернуть сумму чисел между переданными индексами.
# Если индекс выходит за пределы списка, сумма считается до конца и начала списка.


def sum_between_indexes(list_of_numbers, index_1, index_2):
    sum_of_numbers = 0
    if index_1 > index_2:
        index_1, index_2 = index_2, index_1
    for i in range(index_1, index_2 + 1):
        sum_of_numbers += list_of_numbers[i % len(list_of_numbers)]
    return sum_of_numbers


print(sum_between_indexes([1, 2, 3, 4, 5], 0, 2))
print(sum_between_indexes([1, 2, 3, 4, 5], 2, 4))
print(sum_between_indexes([1, 2, 3, 4, 5], 0, 4))
print(sum_between_indexes([1, 2, 3, 4, 5], 0, 10))
