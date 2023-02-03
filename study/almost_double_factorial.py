def almost_double_factorial(n):
    from functools import reduce
    if n == 0:
        return 1
    else:
        num = range(1, n+1, 2)
    return reduce(lambda x, y: x * y, num)

print(almost_double_factorial(0))
print(almost_double_factorial(12))
print(almost_double_factorial(5))
print(almost_double_factorial(6))
print(almost_double_factorial(99))
print(almost_double_factorial(55))
