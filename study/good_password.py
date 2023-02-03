# объявление функции
def is_password_good(password):
    if len(password) < 8:
        return False
    up = low = dig = 0
    for char in password:
        if char.isupper():
            up = 1
        if char.islower():
            low = 1
        if char.isdigit():
            dig = 1
    if up and low and dig:
        return True
    else:
        return False

# считываем данные
txt = input()

# вызываем функцию
print(is_password_good(txt))
