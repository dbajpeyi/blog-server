"""
todo.api

Expose API for our models
"""
import json
from flask.ext.restful import reqparse, Resource
from app.models import *

parser = reqparse.RequestParser()
parser.add_argument('task', type=str)


class DefaultResponseView(Resource):
    """Send a simple response"""
    
    def get(self):
        return {"status": "ok"}
