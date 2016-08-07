#!/usr/bin/env python
# encoding: utf-8

from thermos import app, db
from thermos.models import User

from flask.ext.script import Manager, prompt_bool

manager = Manager(app)

@manager.command
def initdb():
    db.create_all()
    db.session.add(User(username="anbu", email='anbu@example.com'))
    db.session.add(User(username="arun", email='arun@example.com'))
    db.session.commit()
    print 'Initialzed the database'

@manager.command
def dropdb():
    if prompt_bool("Are you sure you want to loose all your data"):
        db.drop_all()
        print "dropped the database"


if __name__ == '__main__':
    manager.run()
