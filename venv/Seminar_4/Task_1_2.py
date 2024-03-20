# Напишите функцию, которая принимает строку текста.
# Сформируйте список с уникальными кодами Unicode каждого символа введенной строки по убыванию.


def unicode_list(text):
    return sorted(set(ord(i) for i in text), reverse=True)


print(unicode_list('Каждый охотник желает знать, где сидит любовник'))
