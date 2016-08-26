#from eve_mongoengine import EveMongoengine
from eve import Eve

#from productdb.app.documents import load_documents
from productdb.app.config import load_config


app = Eve(settings=load_config(env='dev'))
#ext_mongoengine = EveMongoengine(app)
#load_documents(ext_mongoengine.add_model)

if __name__ == '__main__':
    app.run(debug=True)