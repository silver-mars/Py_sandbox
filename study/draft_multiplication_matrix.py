# tests
#matrix_1 = [[1, -1, 0], [3, -4, 2]]
#matrix_2 = [[1, 2], [3, 4], [5, 6]]
#
#matrix_1 = [[1, 2, 1], [0, 1, 0], [2, 3, 4]]
#matrix_2 = [[2, 5], [6, 7], [1, 8]]
#
#matrix_1 = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
#matrix_2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
#
#rows_1, cols_1 = len(matrix_1), len(matrix_1[0])
#rows_2, cols_2 = len(matrix_2), len(matrix_2[0])

rows_1, cols_1 = [int(x) for x in input().split()]
matrix_1 = [[int(x) for x in input().split()] for _ in range(rows_1)]
input()
rows_2, cols_2 = [int(x) for x in input().split()]
matrix_2 = [[int(x) for x in input().split()] for _ in range(rows_2)]


if cols_1 != rows_2:
    print("Количество столбцов первой матрицы не соответствует количеству строк второй матрицы")
    exit()
matrix_3 = [[0 for x in range(cols_2)] for _ in range(rows_1)]

tmp = 0
for c2 in range(cols_2):
    for r1 in range(rows_1):
        for c1 in range(cols_1):
            tmp += matrix_1[r1][c1] * matrix_2[c1][c2]
        matrix_3[r1][c2] = tmp
        tmp = 0

for i in range(rows_1):
    print(*matrix_3[i])
