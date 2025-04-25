from fastapi.testclient import TestClient     #simple way to create a client for our app
from ..main import app
from fastapi import status

client = TestClient(app)   # connecting our client into testclient using app inside main

def test_return_health_check():
    response = client.get("/healthy")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {'status' : 'Healthy'}
