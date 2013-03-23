#!/usr/bin/env python
from flask.ext.script import Server, Manager
from exi.app import app

manager = Manager(app)
manager.add_command("runserver", Server(host="0.0.0.0"))

if __name__ == "__main__":
    manager.run()
