
from app import app

def test_home_page():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200
    assert b"SmartCampus" in response.data

def test_health_endpoint():
    client = app.test_client()
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json["status"] == "healthy"

def test_students_endpoint():
    client = app.test_client()
    response = client.get("/api/students")
    assert response.status_code == 200
    assert isinstance(response.json, list)

def test_add_student():
    client = app.test_client()
    response = client.post(
        "/api/students",
        json={"name": "Test Student", "course": "DevOps"}
    )
    assert response.status_code == 201
    assert response.json["name"] == "Test Student"

def test_invalid_student():
    client = app.test_client()
    response = client.post("/api/students", json={"name": ""})
    assert response.status_code == 400
