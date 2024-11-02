import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_home(client):
    response = client.get('/')
    assert response.status_code == 200
    assert response.get_json() == {"message": "Welcome to the Flask app!"}

def test_greet_valid(client):
    response = client.get('/greet/John')
    assert response.status_code == 200
    assert response.get_json() == {"message": "Hello, John!"}

def test_greet_invalid(client):
    response = client.get('/greet/123')
    assert response.status_code == 400
    assert "Invalid name" in response.get_json()['error']

def test_add_valid(client):
    response = client.post('/add', json={'a': 3, 'b': 5})
    assert response.status_code == 200
    assert response.get_json() == {"result": 8}

def test_add_missing_params(client):
    response = client.post('/add', json={'a': 3})
    assert response.status_code == 400
    assert "Missing required parameters" in response.get_json()['error']

def test_add_invalid_params(client):
    response = client.post('/add', json={'a': 'three', 'b': 'five'})
    assert response.status_code == 400
    assert "Parameters must be integers" in response.get_json()['error']

def test_404(client):
    response = client.get('/unknown')
    assert response.status_code == 404
    assert response.get_json() == {"error": "Not Found"}
