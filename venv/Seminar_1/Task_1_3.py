# Выведите в консоль таблицу умножения от 2х2 до 9х10 как у школьников на тетрадке

MIN = 2
MAX = 10
COL = 4

for i in (MIN, MIN + COL):
    for second in range(MIN, MAX + 1):
        for first in range(i, i + COL):
            print(f'{first :> 6} x {second :> 2} = {first * second :> 3}',end='\t')
        print()
    print()