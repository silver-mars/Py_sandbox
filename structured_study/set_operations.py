# На вход подаётся последовательность неотрицательных целых чисел. Программа выводит те числа, которые встречаются в данной последовательности более одного раза.

nums = input().split()
result = set()

for element in nums:
    if nums.count(element) > 1:
        result.add(int(element))
if result:
    print(*sorted(result))
