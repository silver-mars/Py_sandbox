#from time import perf_counter
#st = perf_counter()

rows, cols = [int(x) for x in input().split()]
matrix = [[0 for x in range(cols)] for _ in range(rows)]
total = rows * cols
count = 0
con_up_x = 0
con_down_x = 0
con_left_y = 0
con_right_y = 0
x = 0
y = 0

while count != total:
    while count != total and y != cols - con_right_y:
        count += 1
        matrix[x][y] = str(count).ljust(3)
        y += 1
    con_up_x += 1
    y -= 1
    x += 1
    while count != total and x != rows - con_down_x:
        count += 1
        matrix[x][y] = str(count).ljust(3)
        x += 1
    con_right_y += 1
    x -= 1
    y -= 1
    while count != total and y != con_left_y - 1:
        count += 1
        matrix[x][y] = str(count).ljust(3)
        y -= 1
    con_down_x += 1
    y += 1
    x -= 1
    while count != total and x != con_up_x - 1:
        count += 1
        matrix[x][y] = str(count).ljust(3)
        x -=1
    con_left_y += 1
    x += 1
    y += 1

for i in range(rows):
    matrix[i][cols-1] = matrix[i][cols-1].rstrip()
    print(*matrix[i])

#print(perf_counter() - st)   # return float
