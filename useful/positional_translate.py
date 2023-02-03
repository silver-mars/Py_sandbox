#/bin/python3
hexidemal = '0123456789ABCDEF'

x = int(input())
while True:
    base = int(input())
    if base < 1 or base > 64:
        print("Введите систему счисления от 2 до 64.")
        continue
    break

result = ''
while x:
    result = hexidemal[x % base] + result
    x //= base

print(result)
