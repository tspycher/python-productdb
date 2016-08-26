__all__ = ['readfeed']

import importlib


def load_commands(manager):
    for command in __all__:
        x = importlib.import_module("%s.%s" % (__name__, command))
        manager.add_command(str(command).lower(), getattr(x, str(command).title())())
