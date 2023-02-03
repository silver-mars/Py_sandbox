octa = '012345678'
hexidemal = '0123456789ABCDEF'
print("Введите число в шестнадцатиричной системе счисления")
string = input().upper()
result = 0

# defense
for char in string:
    if char in hexidemal:
        continue
    else:
        print(f'Буква "{char}" не входит в шестнадцатиричную систему счисления!')

#while string:
    #result = string[-1] * 
def pos16(string):
    result = 0
    count = 0
    for char in string[::-1]:
        result += hexidemal.find(char) * 9 ** count
        count += 1
    return int(result)

print(pos16('88') == pos16('32')+pos16('22')+pos16('16')+pos16('17'))
