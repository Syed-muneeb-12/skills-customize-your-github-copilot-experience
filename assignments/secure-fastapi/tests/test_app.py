import os
import tempfile
from fastapi.testclient import TestClient

from app import app, DB_PATH

client = TestClient(app)


def setup_function():
    # ensure a fresh DB per test run
    if DB_PATH.exists():
        DB_PATH.unlink()


def test_create_and_get_item():
    resp = client.post("/items/", json={"name": "Alpha", "price": 1.5})
    assert resp.status_code == 200
    data = resp.json()
    assert "id" in data
    item_id = data["id"]

    resp = client.get(f"/items/{item_id}")
    assert resp.status_code == 200
    assert resp.json()["name"] == "Alpha"


def test_pagination_and_search():
    client.post("/items/", json={"name": "Beta", "price": 2.0})
    client.post("/items/", json={"name": "BetaTwo", "price": 3.0})
    resp = client.get("/items/?q=Beta&limit=2")
    assert resp.status_code == 200
    data = resp.json()
    assert len(data) >= 2


def test_unauthorized_admin():
    resp = client.post("/admin/secure-action")
    assert resp.status_code == 401
