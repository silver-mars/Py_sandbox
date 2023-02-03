rows, cols = [int(x) for x in input().split()]
matrix = [[0 for x in range(cols)] for _ in range(rows)]
count = 1
curr_row = 0
last = []

for col in range(cols):
    curr_col = col
    while abs(curr_col) != cols or curr_row != cols:
        if curr_row < 0 or curr_col < 0:
            last.append([curr_row, curr_col])
        else:
            matrix[curr_row][curr_col] = str(count).ljust(3)
            count += 1
        curr_row += 1
        curr_col -= 1
        if curr_row == rows:
            curr_row = 0
            break
        if abs(curr_col) == cols:
            curr_col = 0
else:
    for element in last:
        matrix[element[0]][element[1]] = str(count).ljust(3)
        count += 1

for i in range(rows):
    matrix[i][cols-1] = matrix[i][cols-1].rstrip()
    print(*matrix[i], sep='')
