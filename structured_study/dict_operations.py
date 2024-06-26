# Дана последовательность натуральных чисел от 1 до n включительно. 
# Программа группирует все числа данной последовательности по сумме их цифр и определяет длину группы, содержащей наибольшее количество чисел.

# Формат входных данных
# На вход программе подается натуральное число n.

# Формат выходных данных
# Программа должна сгруппировать все числа из натуральной последовательности от 1 до n по сумме их цифр и определить длину группы, содержащей наибольшее количество чисел.

n = int(input())
raw = [str(num) for num in range(1, n+1)]
result = dict()
for element in raw:
    tmp_key = 0
    for char in element:
        tmp_key += int(char)
    if tmp_key in result:
        result[tmp_key] = result.get(tmp_key, []) + [int(element)]
    else:
        result[tmp_key] = [int(element)]
f = lambda num: len(num[1])
length = 0
for values in result.values():
    if len(values) > length:
        length = len(values)
print(length)
