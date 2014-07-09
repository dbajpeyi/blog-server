"""
project.instance

Create and expose the Flask application
"""
from flask import Flask

def create_app(package_name):
    app = Flask(package_name)

    from project.database import db_init
    app.db = db_init()

    from project.routes import routes_init
    routes_init(app)

    return app

app = create_app(__name__)
