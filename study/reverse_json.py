from lxml import etree as et
import json
import base64

class SuperClass():
    def __init__(self, filename):
        with open(filename) as fd:
            self.file = fd.read()
        self.json = json.loads(self.file)
        self.base64 = self.json['data']
        self.data = base64.b64decode(self.base64).decode('utf-8')

    def getxml(self):
        print(self.data)

    def getreverse(self):
        self.xml = et.fromstring(self.data)
        for price in self.xml:
            if not price.get('price'):
                continue
            current = float(price.get('price'))
            if current > 0:
                price.attrib['price'] = f'-{current}'
            elif current < 0:
                price.attrib['price'] = str(current)[1:]
        self.reverse_xml = et.tostring(self.xml, encoding='utf-8', pretty_print=True)
        self.reverse_base64 = base64.b64encode(self.reverse_xml)
        self.new_data = self.reverse_base64.decode('utf-8')
        self.json['data'] = self.new_data
        self.outfile = json.dumps(self.json)
        with open('reverse.json', 'w') as fd:
            fd.write(self.outfile)

if __name__ == '__main__':
    x = SuperClass('reverse.json')
    x.getxml()
    x.getreverse()
    y = SuperClass('reverse.json')
    y.getxml()
