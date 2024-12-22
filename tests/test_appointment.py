from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_no_doctors_available():
    response = client.post(
        "/appointments/", json={"patient_id": 1, "date": "2024-12-25T10:00:00"}
    )
    assert response.status_code == 400
    assert response.json() == {"detail": "No available doctors at the moment"}
