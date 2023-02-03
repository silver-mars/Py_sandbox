rus_alphabet_low = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
rus_alphabet_up = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
eng_alphabet_low = "abcdefghijklmnopqrstuvwxyz"
eng_alphabet_up = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def defense(stack):
    while True:
        swap = input("Укажите смещение в количестве символов\n")
        if not swap.isdigit():
            print("Введите только цифры.")
            continue
        if not 0 < int(swap) <= stack:
            print(f"Введите цифры от 1 до {stack}!")
            continue
        return int(swap)

def crypter(stack, swap):
    result = ''
    for char in string:
        if char.isupper():
            result += up[(up.find(char) + swap) % stack]
        elif char.islower():
            result += low[(low.find(char) + swap) % stack]
        else:
            result += char
    return result

string = input("Введите строку для шифрования\n")
alphabet = input("Выберите алфавит:\neng, rus\n")
encrypt = input("Режим по умолчанию - шифрование.\nЕсли вы желаете провести расшифровку, введите decrypt\n")

if alphabet == 'rus':
    stack = 32
    up = rus_alphabet_up
    low = rus_alphabet_low
else:
    stack = 26
    up = eng_alphabet_up
    low = eng_alphabet_low

swap = defense(stack)
if encrypt == 'decrypt':
    flag = input("Вам известно смещение?")
    if flag == 'no':
        for i in range(stack):
            print(crypter(stack, i))
    else:
        swap = -swap

crypter(stack, i)
