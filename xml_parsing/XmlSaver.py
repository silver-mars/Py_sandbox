from lxml import etree as et

class XmlSaver:

    @staticmethod
    def save_cheque(root, filename):
        cheque = et.tostring(root, encoding='utf-8', pretty_print=True)
        with open(f'src/{filename}', 'w', encoding='utf-8') as fd:
            fd.write(cheque.decode('utf-8'))
