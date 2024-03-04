# Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей.
# Дано a, b, c - стороны предполагаемого треугольника.
# Требуется сравнить длину каждого отрезка-стороны с суммой двух других.
# Если хотя бы в одном случае отрезок окажется больше суммы двух других,
# то треугольника с такими сторонами не существует.
# Отдельно сообщить является ли треугольник разносторонним, равнобедренным или равносторонним

a = int(input('Enter the side a: '))
b = int(input('Enter the side b: '))
c = int(input('Enter the side c: '))

# the existence of a triangle
if c < a + b and b < a + c and a < b + c:
    print('Such a triangle exists')
else: print('There is no such triangle')

# is the triangle versatile
if a != b != c:
    print('It is the triangle versatile')

# is the triangle equilateral
if a == b == c:
    print ('It is the triangle equilateral')

# is the triangle isosceles
elif a == b or b == c or c == a:
    print ('It is the triangle isosceles')