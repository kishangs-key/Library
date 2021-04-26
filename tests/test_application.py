import json
import pytest
from helloworld.run import application

@pytest.fixture
def client():
    return application.test_client()

def test_response(client):
    return "The Website Works Successfully"
