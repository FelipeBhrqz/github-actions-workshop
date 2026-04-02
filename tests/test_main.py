from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_sum_endpoint() -> None:
    response = client.post("/sum", json={"a": 2, "b": 3})
    assert response.status_code == 200
    assert response.json() == {"result": 5}


def test_resta_endpoint() -> None:
    response = client.post("/resta", json={"a": 5, "b": 3})
    assert response.status_code == 200
    assert response.json() == {"result": 2}


def test_multiply_endpoint() -> None:
    response = client.post("/multiply", json={"a": 2, "b": 3})
    assert response.status_code == 200
    assert response.json() == {"result": 6}