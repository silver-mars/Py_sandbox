def base_36(num):
    alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ''

    while num > 0:
        num, m = divmod(num, 36)
        result = alphabet[m] + result
    return result

result = base_36(12376493)
print(result)
