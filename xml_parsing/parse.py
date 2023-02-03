import xml.etree.cElementTree as ET

ns = {"ck": "http://fsrar.ru/WEGAIS/ChequeV3",
      "ns": "http://fsrar.ru/WEGAIS/WB_DOC_SINGLE_01",
      "gz": {"gz": "http://fsrar.ru/WEGAIS/goznak"}}

ns = {"ck": "http://fsrar.ru/WEGAIS/ChequeV3",
      "ns": "http://fsrar.ru/WEGAIS/WB_DOC_SINGLE_01",
      "gz": "http://fsrar.ru/WEGAIS/goznak"}

print(ns)

def parse(filename):
    tree = ET.parse(filename)
    root = tree.getroot()

    print(len(root))

    print('All root tags:')
    for element in root:
        print(element.tag)

    print('All subelement tags:')
    for element in root:
        for subelement in root:
            print(subelement.tag)

    print('All attributes:')
    for element in root:
        for subelement in element:
            print(subelement)

    print('All data:')
    for element in root:
        for subelement in element:
            print(subelement.text)

    element = root.findall('NCode')
    print("findall:")
    if element is None:
        print("element not found")
    else:
        print(element)

    print(ns['gz'])

    print("Again. Only this is meaning")
    for NCode in root.iter('{http://fsrar.ru/WEGAIS/goznak}NCode'):
        print(NCode.tag)

    print("Again. Only this is meaning")
    for NCode in root.findall('.//{http://fsrar.ru/WEGAIS/goznak}NCode', ns):
        print(NCode.text)

    print('final')
    for bc in root.findall('gz:NCode'):
        print(bc)

parse('myGZ.xml')
