import random

num = random.randint(1, 100)
counter = 0

def is_valid():
    x = input()
    if x.isdigit():
        if 1 <= int(x) <= 100:
            return int(x)
    print("Проверьте корректность введённого числа")
    print("Введите число от 1 до 100\n")
    is_valid()

print("Добро пожаловать в числовую угадайку.")
print("Вам предстоит угадать число от 1 до 100")
print("Ваше число?\n")

while True:
    x = is_valid()
    #print(x)
    #print(type(x))
    counter +=1
    if x > num:
        print("Введённое Вами число больше загаданного. Попробуйте ещё раз...")
    elif x < num:
        print("Введённое Вами число меньше загаданного. Попробуйте ещё раз...")
    else:
        print("Поздравляем! Вы угадали!")
        print(f"Число попыток: {counter}")
        break
