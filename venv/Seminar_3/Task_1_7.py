# Пользователь вводит строку теста.
# Подсчитайте сколько раз встречается каждая буква в строке без использования метода count и с ним.
# Результат сохраните в словаре, где ключ - символ, а значение - частота встречи символа в строке.
# Обратите внимание на порядок ключей. Объясните почему они совпадают или не совпадают в ваших решениях.

def count_letters(text):
    letter_counts = {}
    for letter in text:
        if letter in letter_counts:
            letter_counts[letter] += 1
        else:
            letter_counts[letter] = 1
    return letter_counts


data = input('Введите строку теста: ')
print(count_letters(data))
