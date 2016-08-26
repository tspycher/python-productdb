# import mongoengine
# from . import BaseDocument

# class Product(BaseDocument):
#    name = mongoengine.StringField()
#    price = mongoengine.FloatField()

model = {
    'item_title': 'product',
    'additional_lookup': {
        'url': 'regex("[\w]+")',
        'field': 'code'
    },

    # Schema definition, based on Cerberus grammar. Check the Cerberus project
    # (https://github.com/nicolaiarocci/cerberus) for details.
    'schema': {
        'code': {
            'type': 'string',
            'required': True,
        },
        'title': {
            'type': 'string',
            'required': True,
            'minlength': 1,
            #'maxlength': 250, # there are titles longer than 250
        },
        'price': {
            'type': 'number',
            'required': True,
        },
        'description_long': {
            'type': 'string',
            'nullable': True,
        },
        'description_short': {
            'type': 'string',
            'nullable': True,
        },
    }
}
