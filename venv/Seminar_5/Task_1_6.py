# Введите в консоль таблицу умножения от 2х2 до 9х10 как на школьной тетрадке
# Таблицу создайте в виде однострочного генератора, где каждый элемент генератора - отдельный пример таблицы умножения.
# Для вывода результата используйте принт без перехода на новую строку.

MIN = 2
MAX = 10
COL = 4

# for i in (MIN, MIN + COL):
#     for second in range(MIN, MAX + 1):
#         for first in range(i, i + COL):
#             print(f'{first :> 6} x {second :> 2} = {first * second :> 3}',end='\t')
#         print()
#     print()

table_gen = (f'{first :> 6} x {second :> 2} = {first * second :> 3}'
             for first in range(MIN, MAX + 1)
             for second in range(MIN, MAX + 1))

print(*table_gen, sep='\t')