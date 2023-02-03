import datetime

# объявление функции
def is_magic(date):
    source = date.split('.')
    return int(source[0]) * int(source[1]) == int(source[2][2:])

# считываем данные
date = input()

# вызываем функцию
print(is_magic(date))
