"""
todo.models

Schema for mongo documents we will store
"""
from mongoengine import *
    
class Todo(Document):
    """Something we want to do"""
    
    activity = StringField(max_length=128, required=True)
    completed = BooleanField(default=False)

    meta = {
        'indexes': ['activity']
    }

    def __str__(self):
        return self.activity
