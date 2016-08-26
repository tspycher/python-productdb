import importlib
from ..models import load_model, all_models

def load_config(env='dev'):
    config = importlib.import_module("%s.config_%s" % (__name__, env)).config
    for m in all_models():
        config['DOMAIN'][m] = load_model(m)
    return config