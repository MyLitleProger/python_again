# Программа загадывает число от 0 до 1000.
# Необходимо угадать число за 10 попыток.
# Программа должна подсказывать “больше” или “меньше” после каждой попытки.
#
# Для генерации случайного числа используйте код:
# from random import randint
# num = randint(LOWER_LIMIT, UPPER_LIMIT)

from random import randint

num = randint(0, 1000)

i = 1
while i < 10:
    user = int(input('Enter a number from 0 to 1000: '))
    if user == num:
        print('Right!')
        break
    elif user < num:
        print('More!')
    else:
        print('Less!')
    i += 1

print('Bye!')