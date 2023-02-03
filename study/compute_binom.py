# объявление функции
def factorial(num):
    if num == 0:
        return 1
    total = 1
    for i in range(1, num + 1):
        total *= i
    return total

def compute_binom(n, k):
    return int(factorial(n) / (factorial(k) * factorial(n - k)))

# считываем данные
n = int(input())
k = int(input())

# вызываем функцию
print(compute_binom(n, k))
