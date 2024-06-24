# Код размещает в обратном порядке элементы последовательности от элемента с номером X до элемента с номером Y, а затем от элемента с номером A до элемента с номером B.

# Входные данные:

# example input: 9 2 5 6 9
# second example: 9 3 6 5 8

n, X, Y, A, B = [int(num) for num in input().split()]
numbers = list(range(1, n+1))

# 1-ый вариант:
first = list(range(Y, X-1, -1))
numbers[X-1:Y] = first
second = reversed(numbers[A-1:B])
numbers[A-1:B] = second

print(*numbers)

# Упрощённый вариант:

numbers[X-1:Y] = list(range(Y, X-1, -1))
numbers[A-1:B] = reversed(numbers[A-1:B])

print(*numbers)

# 2-ой вариант:

numbers[X-1:Y] = numbers[X-1:Y][::-1]
numbers[A-1:B] = numbers[A-1:B][::-1]

print(*numbers)
