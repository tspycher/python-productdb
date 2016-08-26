#from eve_mongoengine import EveMongoengine
#from productdb.app.documents import load_documents
import os
from eve import Eve
from productdb.app.config import load_config


def create_app(env='dev'):
    app = Eve(
        settings=load_config(env=env),
        static_url_path='/web',
        static_folder=os.path.abspath(os.path.join(os.path.dirname(os.path.realpath(__file__)), '../web')))
    # ext_mongoengine = EveMongoengine(app)
    # load_documents(ext_mongoengine.add_model)
    return app





