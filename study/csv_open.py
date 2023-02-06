def open_csv(name):
    with open(name, 'r') as fd:
        textum = fd.readlines() # Считываем всё как длинный лист, где каждая строка - отдельный список
    attributes = textum[0].replace("\"", "").split(',')
    data = []

    for line in textum[1:]:
        data.append(line.split(','))
