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
    api.add_resource(SavePostView, "/api/post/save", methods=['GET','POST'])

    return api
