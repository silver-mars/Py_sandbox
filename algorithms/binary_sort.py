def binary_sort(massive, seek):
    begin = 0
    end = len(massive) - 1
    while end >= begin:
        mid = int((begin + end) / 2)
        if massive[mid] > seek:
            end = mid - 1
        elif massive[mid] < seek:
            begin = mid + 1
        else:
            return mid
    return None

my_list = [i for i in range(8)]
print(my_list)
print(binary_sort(my_list, 10))
