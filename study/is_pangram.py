# объявление функции
def is_pangram(text):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    for char in alphabet:
        if char not in text.lower():
            return False
    return True

# считываем данные
text = input()

# вызываем функцию
print(is_pangram(text))
