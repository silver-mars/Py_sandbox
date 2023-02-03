list1 = [[1, 7, 8], [9, 7, 102], [102, 106, 105], [100, 99, 98, 103], [1, 2, 3]]
for i in range(len(list1)):
    list1[i].reverse()
print(list1)

list1 = ['a', 'b', ['c', ['d', 'e', ['f', 'g'], 'k'], 'l'], 'm', 'n']
sub_list = ['h', 'i', 'j']

list1[2][1][2].extend(sub_list)
print(list1)

letters = ['a', 'b', 'c', 'd']

#new_letters = letters.copy()
#new_letters = list(letters)
new_letters = letters[:]

print(new_letters)

print(id(letters))
print(id(new_letters))

numbers = [10, 20, 30, 40]
del numbers[0:6]
print(numbers)
