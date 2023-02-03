from lxml import etree

page = etree. Element('html')
doc = etree.ElementTree(page)
head_et = etree.SubElement(page, 'head')
body_et = etree.SubElement(page, 'body')
title = etree.SubElement(head_et, 'title')
title.text = 'Your page title really here'
link_et = etree.SubElement(head_et, 'link', rel='stylesheet', href='mystyle.css', type='text/css')

new_doc = etree.tostring(page, pretty_print=True, encoding='utf-8')
#print(new_doc)
with open('homemade.xml', 'wb') as fd:
    doc.write(fd, pretty_print=True)
