import random

digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_.'
chars = ''

print("Welcome to generation passwords 1.0")
nums = input("What's number passwords are you wish to create?\n")
length = input("What's length one password are you wish?\n")
digit = input("Create from digits?\n")
lower = input(f"Create from lowercase letters?\n{lowercase_letters}\n")
upper = input(f"Create from uppercase letters?\n{uppercase_letters}\n")
symbols = input(f"Create from next symbols?\n{punctuation}\n")
exceptions = input(f"Excepts many-variaty symbols? il1Lo0O\n")

if digit.lower() in ("y", 'yes', 'д', 'да'):
    chars += digits
if lower.lower() in ("y", 'yes', 'д', 'да'):
    chars += lowercase_letters
if upper.lower() in ("y", 'yes', 'д', 'да'):
    chars += uppercase_letters
if symbols.lower() in ("y", 'yes', 'д', 'да'):
    chars += symbols.lower()

def generation_password(length, chars):
    result = ''
    n = len(chars) -1
    for _ in range(int(length)):
        result += random.choice(chars)
    return result

for x in range(int(nums)):
    print(generation_password(length,chars))
