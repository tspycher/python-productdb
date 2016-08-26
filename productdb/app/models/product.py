# import mongoengine
# from . import BaseDocument

# class Product(BaseDocument):
#    name = mongoengine.StringField()
#    price = mongoengine.FloatField()

model = {
    'item_title': 'product',
    'additional_lookup': {
        'url': 'regex("[\w]+")',
        'field': 'title'
    },

    # Schema definition, based on Cerberus grammar. Check the Cerberus project
    # (https://github.com/nicolaiarocci/cerberus) for details.
    'schema': {
        'title': {
            'type': 'string',
            'required': True,
            'minlength': 1,
            'maxlength': 250,
        },
        'price': {
            'type': 'number',
            'required': True,
        },
        'description_long': {
            'type': 'string',

        },
        'description_short': {
            'type': 'string',

        },
    }
}
