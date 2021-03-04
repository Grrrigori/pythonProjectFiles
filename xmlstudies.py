from xml.etree import ElementTree

tree =ElementTree.parse('files//cd_catalog.xml')
root= tree.getroot()

# print(root)
# print(root.tag, root.attrib)
#
# for x in root:
#     print(x.tag, x.attrib)

# print(root[0][6][0].text)
#
# for element in root.iter('CD'):
#     print(element[0].text,element[1].text)

for element in root.iter('SELLS'):
    sold_albums=0
    for child in element:
        sold_albums+= int(child.text)
    print(sold_albums)

cd= root[0]
data=next(cd.iter('Y1985'))
data.text=str(int(data.text)+10000)
print(data.text)

tree.write()

