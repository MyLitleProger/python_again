# Пользователь вводит данные. Сделайте проверку данных
# и преобразуйте если возможно в один из вариантов ниже
# - целое положительное число
# - вещественное положительное или отрицательное число
# - строку в нижнем регистре, если в строке есть хотя бы одна заглавная буква
# - строку в нижнем регистре в остальных случаях

data = input('Введите данные: ')

if data.isdigit():
    new_data = int(data)
elif data.replace('.', '', 1).replace('-', '', 1).isdigit():
    new_data = float(data)
elif data.isupper():
    new_data = data.lower()
else:
    new_data = data.lower()

print(new_data)
print(type(new_data))

