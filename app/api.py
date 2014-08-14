"""
todo.api

Expose API for our models
"""
import json
from flask.ext.restful import reqparse, Resource
from app.models import *

parser = reqparse.RequestParser()



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

class SavePostView(JsonBaseView):
    """
        Save a blog post, which will have a user, title and content
    """

    def get_user(self):
        #todo : create user from request item, build auth system

        user = User(name="Deepankar Bajpeyi", email="dbajpeyi@gmail.com") 
        user.save()
        return user

    def post_as_dict(self, post):
        return  {
            "author"    : unicode(post.author),
            "content"   : post.content,
            "title"     : post.title
        }


    def create_post(self, args):
        title       = args.get("title") 
        content     = args.get("content")
        user        = self.get_user()
        post        = Post(title = title, content = content, author=user)
        post.save()
        return self.post_as_dict(post)

    def post(self):
        parser.add_argument('title', type=str)
        parser.add_argument('content', type=str)
        args = parser.parse_args()
        return self.send_json({"post" : self.create_post(args)})
        
        

