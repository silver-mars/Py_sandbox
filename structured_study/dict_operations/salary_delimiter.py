import csv
import time

start_time = time.perf_counter()
comp_len = {}
comp_sal = {}
total = []
with open('salary_data.csv', encoding='utf-8') as file:
    rows = csv.reader(file, delimiter=';')
    header = next(rows)
    for row in rows:
        comp_sal[row[0]] = comp_sal.get(row[0], 0) + int(row[1])
        comp_len[row[0]] = comp_len.get(row[0], 0) + 1
    for one in comp_len:
        tmp = comp_sal[one] / comp_len[one]
        total.append({'name': one, 'avg': tmp})
    # Сортировка по ключам и значениям словаря
    f = lambda item: (item['avg'], item['name'])
    for company in sorted(total, key=f):
        print(company['name'])
end_time = time.perf_counter()
elapsed_time = end_time - start_time
print("The time is", elapsed_time)
