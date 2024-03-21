# Напишите функцию для транспонирования матрицы


def transpose(matrix):
    return [list(i) for i in zip(*matrix)]


print(transpose([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))