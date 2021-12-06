from fastapi.testclient import TestClient
from starlette import responses

from .app import app

client = TestClient(app)

def test_root():
    response = client.get('/')
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to TokenAPI"}

def test_generation_token():
    response = client.get('/client/scanner/generateur?user=ZENvZGU=&scanner=1')
    assert response.status_code == 200

def test_validation_token():
    response = client.get(
        '/client/scanner/validation?user=ZENvZGU=&scanner=1&date=2021340143735&treatmentId=ZENvZGUxMjAyMTM0MDE0MzczNQ==')
    assert response.json() == {"status":200, "request":"ZENvZGUxMjAyMTM0MDE0MzczNQ==", "result": bool(1)}

