import csv
import time

def condense_csv(filename, id_name):
    with open(filename, encoding='utf-8') as file:
        results = {}
        header = [id_name]
        rows = csv.reader(file)
        for obj, key, value in rows:
            results.setdefault(obj, {}).update({key: value})
            if key not in header:
                header.append(key)

    filename = 'condensed.csv'
    with open(filename, 'w', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(header)
        [writer.writerow([one, *results[one].values()]) for one in results]

start_time = time.perf_counter()
condense_csv('raw_data.csv', 'object')
end_time = time.perf_counter()
elapsed_time = end_time - start_time
print("The time is", elapsed_time)
