# объявление функции
def number_to_words(num):
    list_number = ['ноль', 'один', 'два', 'три', 'четыре', 'пять', 'шесть', 'семь', 'восемь', 'девять']
    list_decimal = ['десять', 'одиннадцать', 'двенадцать', 'тринадцать', 'четырнадцать', 'пятнадцать', 'шестнадцать', 'семнадцать', 'восемнадцать', 'девятнадцать']
    list_decimals = ['null', 'null', 'двадцать', 'тридцать', 'сорок', 'пятьдесят', 'шестьдесят', 'семьдесят', 'восемьдесят', 'девяносто']
    if num < 10:
        return list_number[num]
    elif num < 20:
        return list_decimal[num - 10]
    elif num % 10 == 0:
        return list_decimals[num // 10]
    else:
        return list_decimals[num // 10] + ' ' + list_number[num % 10]

# считываем данные
n = int(input())

# вызываем функцию
print(number_to_words(n))
