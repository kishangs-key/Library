import json
import pytest
from application import create_app

@pytest.fixture
def client():
    return create_app.test_client()

def test_response(client):
    return "The Website Works Successfully"
