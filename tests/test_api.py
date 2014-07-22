"""
tests.test_api

Check all the api's we have exposed and make
sure they behave as we expect
"""
import os
import unittest
import json


def test_landing_page(app):
    """Test /api/v1/todos"""

    resp =  app.client.get("/api/v1/default")
    assert resp.status_code == 200
    assert resp.content_type == 'application/json'
