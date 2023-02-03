n = int(input())
pascal_binom = [[1], [1, 1]]

count = 1
while count < n:
    for i in range(count):
        tmp = [1]
        tmp.append(pascal_binom[count][i] + pascal_binom[count][i+1])
        tmp.append(1)
    pascal_binom.append(tmp)
    count += 1
print(pascal_binom[n])
