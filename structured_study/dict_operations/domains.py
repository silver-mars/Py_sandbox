import csv

domens = {}
with open('data.csv', encoding='utf-8') as file:
    rows = csv.reader(file)
    header = next(rows)
    for row in rows:
        begin = row[2].find('@') + 1
        domen = row[2][begin:]
        domens[domen] = domens.get(domen, 0) + 1

# Сортировка по двум значениям сразу
f = lambda item: (item[1], item[0])
result = []
# Так как item возвращает кортеж, эту анонимную функцию можно передать в качестве ключа к sorted
for domen, quantity in sorted(domens.items(), key=f):
    result.append({'domain': domen, 'count': quantity})
filename = 'domain_usage.csv'
columns = ['domain', 'count']

with open(filename, 'w', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=columns)
    writer.writeheader()
    for row in result:
        writer.writerow(row)
