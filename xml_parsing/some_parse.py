from lxml import etree

ns = {"ck": "http://fsrar.ru/WEGAIS/ChequeV3",
      "ns": "http://fsrar.ru/WEGAIS/WB_DOC_SINGLE_01",
      "gz": "http://fsrar.ru/WEGAIS/goznak"}

doc = etree.parse('myGZ.xml')
#print(etree.len(doc))

par = doc.find('//{http://fsrar.ru/WEGAIS/goznak}NCode', namespaces=ns)
print(par.text)

text = doc.findtext('//{http://fsrar.ru/WEGAIS/goznak}NCode', namespaces=ns)
print(text)

# длина поля bc (аналог MarkInfo)
bc = doc.find('.//{http://fsrar.ru/WEGAIS/goznak}bc', ns)
print(len(bc))
print(bc)
barcodes = bc.getchildren() # получить список всех детей узла bc
for element in barcodes:
    print(element.text)

for el in doc.getiterator(): # итерировать вообще каждый элемент.
    print(el.tag)

print("Нижеследующий участок кода не работает, не знаю отчего.")
walk = doc.getiterator('.//{http://fsrar.ru/WEGAIS/goznak}NCode')
print(walk)
for el in walk:
    print(el.tag)
