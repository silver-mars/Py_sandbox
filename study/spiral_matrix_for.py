rows, cols = [int(x) for x in input().split()]
matrix = [[0 for x in range(cols)] for _ in range(rows)]
total = rows * cols
count = 0
con_up_x = 0
con_down_x = 0
con_left_y = 0
con_right_y = 0

while count != total:
    for i in range(con_left_y, cols - con_right_y):
        count += 1
        matrix[con_up_x][i] = str(count).ljust(3)
    con_up_x += 1
    for i in range(con_up_x, rows - con_down_x):
        count += 1
        matrix[i][cols - con_right_y - 1] = str(count).ljust(3)
    con_right_y += 1
    if count == total:
        break
    for i in range(cols - con_right_y - 1, con_left_y - 1, -1):
        count += 1
        matrix[rows - con_down_x - 1][i] = str(count).ljust(3)
    con_down_x += 1
    for i in range(rows - con_down_x - 1, con_right_y - 1, -1):
        count += 1
        matrix[i][con_left_y] = str(count).ljust(3)
    con_left_y += 1

for i in range(rows):
    matrix[i][cols-1] = matrix[i][cols-1].rstrip()
    print(*matrix[i])
