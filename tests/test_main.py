"""Tests for the main FastAPI application."""

from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_root():
    """Test the root endpoint."""
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to FastAPI GitOps Starter!"}


def test_health_check():
    """Test the health check endpoint."""
    response = client.get("/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "healthy"
    assert data["service"] == "fastapi-gitops-starter"


def test_list_items():
    """Test the list items endpoint."""
    response = client.get("/api/items")
    assert response.status_code == 200
    data = response.json()
    assert "items" in data
    assert len(data["items"]) == 3
    assert data["items"][0]["id"] == 1


def test_get_item():
    """Test the get item endpoint."""
    response = client.get("/api/items/5")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == 5
    assert data["name"] == "Item 5"
    assert "item number 5" in data["description"]


def test_create():
    """Test the create endpoint"""
    # todo = {"name": "test_name", "description": "Buy milk"}
    # response = client.post("/api/items", json=todo)
    response = client.post("/api/items?name=test_name&description=Buy+milk")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == 999
    assert data["name"] == "test_name"
    assert data["description"] == "Buy milk"
    # response = client.get("/api/items/999")
    # assert response.status_code == 200
    # data = response.json()
    # assert data["name"] == "test_name"
    # assert data["description"] == "Buy milk"
