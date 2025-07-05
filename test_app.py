import json
from app import app

def test_get_tasks():
    client = app.test_client()
    response = client.get("/tasks")
    assert response.status_code == 200
    assert isinstance(response.get_json(), list)

def test_add_task():
    client = app.test_client()
    response = client.post("/tasks", json={"title": "Yeni görev", "done": False})
    data = response.get_json()
    assert response.status_code == 201
    assert data["title"] == "Yeni görev"
    assert not data["done"]
