# Сделать елочку из звезд, количество рядов определяет пользователь

SPACE = ' '
STAR = '*'
row = int(input('Введите высоту елочки: '))
spaces = row - 1
stars = 1

for i in range(row):
    print(SPACE * spaces + stars * STAR)
    spaces -= 1
    stars += 2