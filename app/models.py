"""
app.models

Schema for mongo documents we will store
"""
from mongoengine import *
import datetime
    
class User(Document):
    name        = StringField(max_length=50, required=True)
    email       = EmailField(max_length=50, required=True)

    def __unicode__(self):
        return self.name


class Post(Document):
    """A combination of title , content and author"""
    
    author      = ReferenceField(User, required=True)
    content 	= StringField(max_length=10000, required=True)
    title       = StringField(max_length=250, required=True)
    created     = DateTimeField(default=datetime.datetime.now(), required=True)
    completed 	= BooleanField(default=False)

    meta = {
        'indexes': ['title', '-created']
    }

    def __str__(self):
        return self.title

class Comment(Document):
    text        = StringField(max_length=255, required=True) 
    user        = ReferenceField(User, required=True)

    def __unicode__(self):
        return "%s : %s"(user, text)

