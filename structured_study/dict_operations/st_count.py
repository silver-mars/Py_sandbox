import csv

in_filename = 'student_counts.csv'
out_filename = 'sorted_student_counts.csv'

with open(in_filename, encoding='utf-8') as inp, \
    open(out_filename, 'w', encoding='utf-8') as outp:
    rows = csv.DictReader(inp)
    header = rows.fieldnames[1:]
    f = lambda item: (int(item.split('-')[0]), item[-1])
    new_header = ['year'] +  sorted(header, key=f)
    writer = csv.DictWriter(outp, fieldnames=new_header)
    writer.writeheader()
    new_order = {}
    result = []
    for i, row in enumerate(rows):
        for key in new_header:
            new_order.setdefault(i, {}).update({key: row[key]})

        writer.writerow(new_order[i])
        #result.append(new_order[i])
    #print(*result, sep='\n')
