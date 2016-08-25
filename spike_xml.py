from lxml import etree
import json

parser = etree.XMLParser(recover=True) #recovers from bad characters.
tree = etree.parse('data/feed.xml', parser)

products = []
for elem in tree.iter("product"):
    product = {}
    product['features'] = {}
    for f in elem.iter("feature"):
        label = f.findtext('label', default=None)
        value = f.findtext('value', default=None)
        product['features'][label] = value
    for c in elem.getchildren():
        product[c.tag] = c.text

    products.append(product)

print json.dumps(products, indent=4)