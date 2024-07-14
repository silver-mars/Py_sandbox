import csv

filename = 'wifi.csv'
counts = {}
with open(filename, encoding='utf-8') as file:
    rows = csv.reader(file, delimiter=';')
    headers = next(rows)
    for row in rows:
        counts[row[1]] = counts.get(row[1], 0) + int(row[-1])
    # Сортировка по двум значениям: DESC и ASC
    f = lambda item: (-item[1], item[0])
    for district, counts in sorted(counts.items(), key=f):
        print(f"{district}: {counts}")
