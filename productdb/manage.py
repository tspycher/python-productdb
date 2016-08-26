from flask.ext.script import Manager
from productdb.app import create_app
from productdb.app.commands import load_commands

app = create_app('dev')
manager = Manager(app)

load_commands(manager=manager)

if __name__ == "__main__":
    manager.run()