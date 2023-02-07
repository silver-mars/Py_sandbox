from lxml import etree as et
from json import loads
import base64
import sh

filename = '1234.log'
seek = 'DEBUG r.c.c.q.Main [main] finish create json'

with open(filename) as fd:
    logs = fd.readlines()

for line in logs:
    if seek not in line:
        continue
    begin = line.find('{')
    end = line.find('}') + 1
    json = loads(line[begin:end])

    date = json['date']
    if not sh.find("-type", "d", "-name", date):
        sh.mkdir(date)
    uri = json['uri']
    b64_json = json['data']
    cheque = base64.b64decode(b64_json).decode('utf-8')
    with open(f'{date}/{uri}', 'w') as fd:
        fd.write(cheque)
