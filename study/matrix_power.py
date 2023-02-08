matrix_1 = [[1, 0],
            [4, 1]]

#rows_1 = int(input())
#matrix_1 = [[int(x) for x in input().split()] for _ in range(rows_1)]
matrix_2 = [[0 for x in range(len(matrix_1))] for _ in range(len(matrix_1))]
power = int(input())

rows_1, cols_1 = len(matrix_1), len(matrix_1[0])
rows_2, cols_2 = len(matrix_2), len(matrix_2[0])

for i in range(len(matrix_1)):
    for j in range(len(matrix_1)):
        matrix_2[i][j] = matrix_1[i][j]

matrix_3 = [[0 for x in range(cols_1)] for _ in range(rows_1)]

count = 1
while count != power:
    tmp = 0
    for c2 in range(cols_1):
        for r1 in range(rows_1):
            for c1 in range(cols_1):
                tmp += matrix_1[r1][c1] * matrix_2[c1][c2]
            matrix_3[r1][c2] = tmp
            tmp = 0
    for i in range(rows_1):
        for j in range(cols_1):
            matrix_1[i][j] = matrix_3[i][j]
    count += 1

for i in range(rows_1):
    print(*matrix_1[i])
