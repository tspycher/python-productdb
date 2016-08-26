from lxml import etree
import json

parser = etree.XMLParser(recover=True) #recovers from bad characters.
tree = etree.parse('data/feed.xml', parser)

products = []
ids = []
for elem in tree.iter("product"):
    product = {}
    product['productfeatures'] = {}
    for f in elem.iter("feature"):
        label = f.findtext('label', default=None)
        value = f.findtext('value', default=None)
        product['productfeatures'][label] = value
    for c in elem.getchildren():
        product[c.tag] = c.text
    #print json.dumps(product, indent=4)
    products.append(product)
    id_field = 'code' #'cnetID'
    if not product[id_field] in ids:
        ids.append(product[id_field])
    else:
        print "DUBBLE ID"

print ids
#print json.dumps(products, indent=4)