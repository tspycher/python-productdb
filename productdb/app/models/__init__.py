__all__ = ['product']
#import mongoengine

#class BaseDocument(mongoengine.Document):
#    meta = {
#        'allow_inheritance': True,
#        #'strict': False
#    }

#from product import Product

import importlib

def all_models():
    return __all__

def load_model(model):
    return importlib.import_module("%s.%s" % (__name__, model)).model
