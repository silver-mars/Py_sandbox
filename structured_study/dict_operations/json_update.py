import json

filename='data.json'
fileout='updated_data.json'
with open(filename, encoding='utf-8') as file:
    raw = json.load(file)

conv_dict = {
    str: lambda x: x + '!',
    bool: lambda x: not x,
    int: lambda x: x + 1,
    list: lambda x: x * 2,
    dict: lambda x: {**x, "newkey": None}
}

result = []
for line in raw:
    if type(line) in conv_dict:
        result.append(conv_dict[type(line)](line))

with open(fileout, 'w', encoding='utf-8') as out:
    json.dump(result, out, indent=3)
