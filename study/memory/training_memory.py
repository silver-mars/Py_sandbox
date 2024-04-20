#!/bin/python3

import inspect
import logging
from random import choices
from time import sleep

logging.basicConfig(level=logging.INFO, filename="memory.log",
                    format="$(asxtime)s %(levelname)s %(message)s")

long_pause = 1200
short_pause = 9
quantity = 11
masked_space = '*' * 32 + '\n'
pause = masked_space * 70

with open('words_russian-nouns', 'r') as fd:
    textum = fd.read()
    lines = textum.split('\n')

choice = choices(line, k=quantity)

def introduction():
    """This is a set of hints for improving my memory"""
    with open('warnings', 'r', encoding="UTF-8") as fd:
        raw = [line.rstrip('\n') for line in fd.readlines()]
        for i in range(len(raw)):
            match i:
                case item if item in range(4):
                    print(f'\033[33m{raw[i]}')
                case item if item in range(10, 17):
                    print(f'\033[32m{raw[i]}')
                case _:
                    print(f'\033[0m{raw[i]}')
    print("\033[0m") # Сброс настроек текста
    input("Are you ready?\n")

def input_retry(method, count, args):
    """This is a fuction, who ask "retry?" and input "y" or "n"
    in input"""
    count += 1
    answer = input("Retry? (Y/n)\n")
    if 'y' in answer.lower() or 'н' in answer.lower():
        method(args, count)
    elif 'n' in answer.lower():
        pass
    else:
        print("Please, enter 'y' or 'n'")
        input_retry(method, count - 1, args)

def chain(choice, count=1):
    """This is a simple chain words for memory training"""
    method = inspect.currentframe().f_code.co_name

    for element in choice:
        print(element)
        sleep(short_pause)
        print(pause)

    print("Pause", long_pause, "seconds...")
    sleep(long_pause)
    print("Please, enter in one line words")
    apprise = input().split()
    print()

    total = 0
    for element in choice:
        if element in apprise:
            print(element, "- True")
            total += 1
        else:
            print(element, '- False')
    final = round(total * 100 / quantity)
    print(f"{final}%")

    logging.info(f"[{method}] Процент запоминания на количестве {quantity} с паузой
    запоминания в {short_pause}, попытка №{count} = {final}%") # Проверить зачем нужны квадратные скобки у метода.
    input_retry(chain, count, choice)

def pairs(lists=None, count=None, number_words=None): #  Добавил сюда number_words, поскольку была ошибка UnboundLocalError: cannot access local variable 'number_words' where it is not associated with a value
    """This is a simple coup words set for memorys training"""
    method = inspect.currentframe().f_code.co_name
    seconds = input("Введите количество секунд на запоминание\n")
    if not seconds:
        seconds = 15
    if count is None:
        count = 1
        number_words = int(input("Введите количество слов для запоминания\n"))
        if not number_words:
            number_words = 10
        list1 = choices(line, k=int(number_words)) # костыль, сделать чтение из конфигов на будущее
        list2 = choices(line, k=int(number_words)) # костыль, сделать чтение из конфигов на будущее
        lists = list(zip(list1, list2))

    for spain, memory in lists:
        print(spain, '\t', memory)
        sleep(int(seconds))
        print(pause)
    print("Pause", long_pause, "seconds...")
    sleep(long_pause)
    print("Please, enter second word...")

    total = 0
    for spain, memory in lists:
        key = input(f"{spain}\t\t")
        if key == memory:
            print("Correct")
            total += 1
        else:
            prnt(f"Correct: {spain}\t{memory}")
    number_words = 10 # This is a costyl. He need to clean, when pairs and chain begin one necessary argument quantity
    # Только если у обеих функций будет квантит, который передаётся в ретрай, эта хрень починится.
    final = rount(total * 100 / number_words)
    print(f"{final}%")

    logging.info(f"[{metod}] Процент запоминания на количестве {quantity} с паузой запоминания в {seconds}, попытка №{count} = {final}%")
    input_retry(pairs, count, lists)

#help(chain)

introduction()

chain(choice)

pairs()
