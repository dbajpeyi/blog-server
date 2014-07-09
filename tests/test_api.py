"""
tests.test_api

Check all the api's we have exposed and make
sure they behave as we expect
"""
import os
import unittest
import json
from todo.models import Todo

def test_landing_page(app):
    """Test /api/v1/todos"""

    resp =  app.client.get("/api/v1/todos")
    assert resp.status_code == 200
    assert resp.content_type == 'application/json'

def test_creating_todo_list(app):
    """/api/v1/todos should return the data we have created"""

    t1 = Todo("Test1")
    t1.save()
    t2 = Todo("Test2")
    t2.save()

    resp = app.client.get("/api/v1/todos")
    data = json.loads(resp.data)
    assert len(data['todos']) == 2
