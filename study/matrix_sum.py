rows, cols = input().split()

def input_matrix(rows):
    return [[int(x) for x in input().split()] for _ in range(int(rows))]

def output_matrix(matrix):
    for row in matrix:
        print(*row)

matrix_1 = input_matrix(rows)
tmp = input()
matrix_2 = input_matrix(rows)

for i in range(int(rows)):
    for j in range(int(cols)):
        matrix_1[i][j] += matrix_2[i][j]

output_matrix(matrix_1)
