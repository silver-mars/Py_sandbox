with open('mirddin_memory') as fd:
    text = fd.read().splitlines() # Splitlines берёт на вход строку и разделяет её по переносам строк на разные значения в листе.

dic_names = {}
for line in text:
    key, value = line.split(":")
# Нужно добавить в словарь и выполнить проверку.
    #print(parse['Users']['1963863413'])
