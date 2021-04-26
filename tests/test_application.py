import json
import pytest
from helloworld.app import create_app

config_name = os.getenv('FLASK_CONFIG')
app = create_app(config_name)

def client():
    return create_app.test_client()

def test_response(client):
    return "The Website Works Successfully"
