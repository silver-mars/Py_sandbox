# объявление функции is_prime
def is_prime(num):
    if num == 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

# объявление функции get_next_prime
def get_next_prime(num):
    while True:
        num += 1
        if is_prime(num):
            return num

# считываем данные
n = int(input())

# вызываем функцию
print(get_next_prime(n))
