# Продолжаем решать задачу 2.
# Возьмите словарь, который вы получили. Сохранив его итератор.
# Далее выведите первые 5 пар ключ-значение, обращаясь к итератору, а не ключу.


def print_first_five_pairs(dictionary):
    for i in range(5):
        print(*next(dictionary))


text = input("Enter text: ")

my_dict = dict(zip(text, map(ord, text)))
print(my_dict)
print_first_five_pairs(iter(my_dict.items()))
