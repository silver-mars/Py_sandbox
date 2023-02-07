import datetime
import random
import uuid

alnum = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
alphabet_up = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
alphabet_low = 'abcdefghijklmnopqrstuvwxyz'

def random_len(num):
    result = str(random.randint(1, 9))
    for i in range(num - 1):
        result += str(random.randint(0, 9))
    return result

def random_alpha(num):
    result = ''
    for i in range(num):
        result += random.choice(alphabet_up)
    return result

def random_alnum(num):
    result = ''
    for i in range(num):
        result += random.choice(alnum)
    return result

def get_date():
    return str(datetime.date.today())

def get_timestamp():
    return str(datetime.datetime.now().isoformat(timespec='seconds'))

def get_uuid():
    return str(uuid.uuid1())

def base36encode(code, length):
    base36 = ''
    while code != 0:
        code, i = divmod(code, len(alnum))
        base36 = alnum[i] + base36
    count = len(base36)
    while count < length:
        base36 = '0' + base36
        count += 1
    return base36

class Bar:

    def get_150alc(self, cod, length):
        mark = '100'
        number = random_len(8)
        yy = str(datetime.date.today().year)[-2:]
        mm = str(datetime.date.today().month)[-2:]
        if len(mm) < 2:
            mm = '0' + mm
        version = random_len(3)
        krypton = random_alnum(125)
        barcode = str(cod) + mark + number + mm + yy + version + krypton
        return [barcode + f'{i:04}' for i in range(length)]

    def get_oldcod(self, length):
        k_alcode = base36encode(int(random_len(17)), 16)
        okpo = base36encode(int(random_len(5)), 4)
        yy = str(datetime.date.today().year)[-1]
        mm = str(datetime.date.today().month)[-2:]
        dd = str(datetime.date.today().day)[-2:]
        num = random_len(3)
        krypta = random_alnum(31)
        result = []
        for i in range(length):
            marka = f"22N{k_alcode}{okpo}{yy}{mm}{dd}{num}{krypta}{i:06}"
            result.append(marka)
        return result

if __name__ == "__main__":
    x = Bar()
    new_mark = x.get_150alc(500, 10)
    print(type(new_mark))
    print(*new_mark, sep='\n')
    old_mark = x.get_oldcod(10)
    print(type(old_mark))
    print(*old_mark, sep='\n')
