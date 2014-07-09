#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
test.conftest
~~~~~~~~~~~~~~

Setup tests to use a new database and drop the database
after tests complete
"""
import pytest
from flask import Flask
from mongoengine import connect
from project import conf

def db_name():
    return conf.MONGO_DBNAME+"_test"

@pytest.fixture(scope='session')
def app(request):
    app = Flask(__name__)
    app.client = app.test_client()
    app.db = connect(**{'db': db_name()})

    from project.routes import routes_init
    routes_init(app)

    def teardown():
        app.db.drop_database(db_name())

    request.addfinalizer(teardown)
    return app
