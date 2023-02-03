for i in range(1, 14):
    for j in range(1, 13):
        for k in range(1, 12):
            if i * 28 + j * 30 + k * 31 == 365:
                print(i, j, k)
