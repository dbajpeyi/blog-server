"""
project.routes

Bind the api's to the endpoints
"""
from flask.ext.restful import Api
from app.api import *

def routes_init(app):
    api = Api(app)

    api.add_resource(DefaultResponseView, "/api/default")
    api.add_resource(PostListView, "/api/posts")

    return api
