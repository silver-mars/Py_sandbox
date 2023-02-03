for a in range(1, 151):
    for b in range(1, 151):
        if a > b:
            continue
        for c in range(1, 151):
            if b > c:
                continue
            for d in range(1, 151):
                if c > d:
                    continue
                for e in range(1, 151):
                    if d >= e or c >= e or b >= e or a >= e:
                        continue
                    if a ** 5 + b ** 5 + c ** 5 + d ** 5 == e ** 5:
                        print(a, b, c, d, e)
                        print(a + b + c + d)
                        break
