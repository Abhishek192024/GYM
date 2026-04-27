import pytest
from flask import Flask
import sys
import os

# manually app.py ka path add kar rahe hain
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import app as myapp   # <-- yahan change kiya

@pytest.fixture
def client():
    myapp.app.testing = True
    return myapp.app.test_client()

def test_home(client):
    response = client.get('/')
    assert response.status_code == 200

def test_members(client):
    response = client.get('/members')
    assert response.status_code == 200