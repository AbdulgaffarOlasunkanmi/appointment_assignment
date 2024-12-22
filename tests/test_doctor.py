from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_set_doctor_availability():
    response = client.put("/doctors/availability/1",
                          json={"is_available": False})
    assert response.status_code == 200
    assert response.json()["is_available"] == False
