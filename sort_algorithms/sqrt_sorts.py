def insert_sort(A):
    """ сортировка списка A вставками """
    pass

def choice_sort(A):
    """ сортировка списка A выбором """
    pass

def bubble_sort(A):
    """ сортировка списка A методом пузырька """
    pass

def test_sort(sort_algorithm):
    print("Тестируем:", sort_algorithm.__doc__)
    print("Testcase #1: ", end='')
    A = [4, 2, 5, 1, 4]
    A_sorted = [1, 2, 3, 4, 5]
    sort_algorithm(A)
    print("Success" if A == A_sorted else "Fail")

    print("Testcase #2: ", end='')
    A = list(range(10, 40)) + list(range(-10, 10))
    A_sorted = list(range(-10, 40))
    sort_algorithm(A)
    print("Success" if A == A_sorted else "Fail")

    print("Testcase #3: ", end='')
    A = [78, -32, 5, 39, 58, -5, -63, 57, 72, 9, 53, -1, 63, -97, -21, -94, -47, 57, -8, 60, -23, -72, -22, -79, 90, 96, -41, -71, -48, 84, 89, -96, 41, -16, 94, -60, -64, -39, 60, -14, -62, -19, -3, 32, 98, 14, 43, 3, -56, 71, -71, -67, 80, 27, 92, 92, -64, 0, -77, 2, -26, 41, 3, -31, 48, 39, 20, -30, 35, 32, -58, 2, 63, 64, 66, 62, 82, -62, 9, -52, 35, -61, 87, 78, 93, -42, 87, -72, -10, -36, 61, -16, 59, 59, 22, -24, -67, 76, -94, 59]
    A_sorted = [-97, -96, -94, -94, -79, -77, -72, -72, -71, -71, -67, -67, -64, -64, -63, -62, -62, -61, -60, -58, -56, -52, -48, -47, -42, -41, -39, -36, -32, -31, -30, -26, -24, -23, -22, -21, -19, -16, -16, -14, -10, -8, -5, -3, -1, 0, 2, 2, 3, 3, 5, 9, 9, 14, 20, 22, 27, 32, 32, 35, 35, 39, 39, 41, 41, 43, 48, 53, 57, 57, 58, 59, 59, 59, 60, 60, 61, 62, 63, 63, 64, 66, 71, 72, 76, 78, 78, 80, 82, 84, 87, 87, 89, 90, 92, 92, 93, 94, 96, 98]
    sort_algorithm(A)
    print("Success" if A == A_sorted else "Fail")

if __name__ == "__main__":
    test_sort(insert_sort)
    test_sort(choice_sort)
    test_sort(bubble_sort)
