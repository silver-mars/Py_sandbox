for i in range(1, 10):
    for j in range(1, 20):
        for k in range(1, 200):
            if i * 10 + j * 5 + k * 0.5 == 100 and i + j + k == 100:
                print(i, j, k)
