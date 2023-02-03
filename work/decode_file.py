import xml.etree.ElementTree as et
from sys import argv

tree = et.parse(argv[1])
tree.write(
   "./claimissuefsm.xml", xml_declaration=True,
   encoding='utf-8', method="xml")
