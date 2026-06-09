import pytest
from fastapi.testclient import TestClient

from starter_code import app


client = TestClient(app)


def test_create_and_get_item():
    item = {"id": 1, "name": "Test", "price": 5.0}
    resp = client.post("/items/", json=item)
    assert resp.status_code == 200
    data = resp.json()
    assert data["id"] == 1

    resp = client.get("/items/1")
    assert resp.status_code == 200
    data = resp.json()
    assert data["name"] == "Test"


def test_list_pagination_and_filter():
    # add more items
    client.post("/items/", json={"id": 2, "name": "Another", "price": 3.5})
    resp = client.get("/items/?q=Another")
    assert resp.status_code == 200
    data = resp.json()
    assert any(i["id"] == 2 for i in data)


def test_not_found():
    resp = client.get("/items/999")
    assert resp.status_code == 404
