#!/bin/python3

# объявление функции
def merge(list1, list2):
    final_list = []
    while len(list1) != 0 and len(list2) != 0:
        if list1[0] < list2[0]:
            tmp = list1.pop(0)
        else:
            tmp = list2.pop(0)
        final_list.append(tmp)
    final_list = final_list + list1 + list2
    return final_list

# считываем данные
#numbers1 = [int(c) for c in input().split()]
#numbers2 = [int(c) for c in input().split()]
numbers1, numbers2 = [1, 2, 3], [5, 6, 7, 8]
# вызываем функцию
print(merge(numbers1, numbers2))
