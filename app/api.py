"""
todo.api

Expose API for our models
"""
import json
from flask.ext.restful import reqparse, Resource
from app.models import *

parser = reqparse.RequestParser()
parser.add_argument('task', type=str)



class JsonBaseView(Resource):
    
    def send_error(self, e):
        return {
                "error" : e,
                "status": "error",
            }

    def send_json(self, context):
        return context
    

class DefaultResponseView(Resource):
    """Send a simple response"""
    
    def get(self):
        return {"status": "ok"}


class PostListView(JsonBaseView):
    """
        All the posts in the db
    """

    def post_as_dict(self, post):
        return  {
            "author"    : unicode(post.author),
            "content"   : post.content,
            "title"     : post.title
        }

    def get(self):
        resp = []
        for post in Post.objects():
            resp.append(self.post_as_dict(post))
        return self.send_json({"posts": resp})
        

