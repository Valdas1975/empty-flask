import pytest
import os
from main import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    os.environ['TESTING'] = "1"
    client = app.test_client()

    yield client

def test_index(client):
    response = client.get('/')

    assert b'html' in response.data
