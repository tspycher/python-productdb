import os
from lxml import etree
from flask.ext.script import Command, Option
from flask import current_app


class Readfeed(Command):
    """
    Reads the given feed.xml and upserts the data
    """
    EVE_RESOURCE = 'product'

    XML_ELEM_PRODUCT = 'product'
    XML_ELEM_FEATURE = 'feature'
    XML_ELEM_LABEL = 'label'
    XML_ELEM_VALUE = 'value'
    XML_ELEM_ID = 'code'

    option_list = (
        Option('--file', '-f', dest='file', default='../data/feed.xml'),
    )

    def run(self, file):
        logger = current_app.logger
        file = os.path.abspath(os.path.join(os.getcwd(), file))
        for p in self.readFile(file):
            existing = current_app.data.find_one(Readfeed.EVE_RESOURCE, None, code=p[Readfeed.XML_ELEM_ID])
            doc = {'title':p['name'], 'description_long': p['description'], 'description_short': p['shortDescription'],
                   'price': float(p['price']), 'code': p['code']}
            if not self.validator.validate(doc):
                logger.critical("Could not validate new document (%s)" % (self.validator.errors))
                continue

            if not existing:
                obj = current_app.data.insert(Readfeed.EVE_RESOURCE, doc)
                logger.info("Inserted new Document %s" % (str(obj)))
            else:
                current_app.data.update(Readfeed.EVE_RESOURCE, existing['_id'], doc)
                logger.info("Updated Document %s" % (existing['_id']))

    def readFile(self, file):
        parser = etree.XMLParser(recover=True)  # recovers from bad characters.
        tree = etree.parse(file, parser)
        for elem in tree.iter(Readfeed.XML_ELEM_PRODUCT):
            product = {'name':None, 'description':None, 'shortDescription':None, 'price':None}
            product['productfeatures'] = {}
            for f in elem.iter(Readfeed.XML_ELEM_FEATURE):
                label = f.findtext(Readfeed.XML_ELEM_LABEL, default=None)
                value = f.findtext(Readfeed.XML_ELEM_VALUE, default=None)
                product['productfeatures'][label] = value
            for c in elem.getchildren():
                product[c.tag] = c.text
            yield product

    _validator = None
    @property
    def validator(self):
        if not self._validator:
            resource_def = current_app.config['DOMAIN'][Readfeed.EVE_RESOURCE]
            schema = resource_def['schema']
            self._validator = current_app.validator(schema, Readfeed.EVE_RESOURCE)
        return self._validator