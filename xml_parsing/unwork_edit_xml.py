import time
import lxml.etree as ET

def editXML(filename):
    """
    Edit xml-file on example cheque version 3
    """
    # считываем эталонный файл-клейм
    with open(filename, 'r') as file:
        xml = file.read()
    # парсим файл в объект
    doc = ET.fromstring(xml.encode())
    # прописываем нейм спейсы в соотвествии с префиксами
    dict_of_ns = {
        "ck": {'ck': "http://fsrar.ru/WEGAIS/ChequeV3"},
        "ns": {'ns': "http://fsrar.ru/WEGAIS/WB_DOC_SINGLE_01"}
    }
    # меняем значения нужных полей
    (doc.xpath('//ck:Barcode', namespaces=dict_of_ns["ck"])[0]).text = 'forever'
    #(doc.xpath('//rpp:NUMBER', namespaces=dict_of_ns["rpp"])[0]).text = number
    # пишем из объекта в файл.
    ext = ET.tostring(doc, pretty_print=True, encoding='utf-8', xml_declaration=True)
    print("Уже решал этот вопрос, но надо пересмотреть и дообновить, чтобы были все методы собраны в наличии")
    with open('update.xml', 'wb') as fd:
        file.write(ext)
    #r = requests.post(f'{path}', files={'xml_file': ET.tostring(doc, pretty_print=True, encoding='utf-8', xml_declaration=True)})

editXML('Cheque_v3.xml')
