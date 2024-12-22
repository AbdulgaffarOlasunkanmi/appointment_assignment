import pytest


def test_create_patient(client):
    response = client.post(
        "/patients/",
        json={
            "name": "John Doe",
            "age": 30,
            "sex": "male",
            "weight": 70.5,
            "height": 175.0,
            "phone": "1234567890"
        }
    )
    assert response.status_code == 200
    assert response.json()["name"] == "John Doe"


def test_get_all_patients(client):
    response = client.get("/patients/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_get_patient(client):
    # Create a patient
    client.post(
        "/patients/",
        json={
            "name": "Jane Doe",
            "age": 25,
            "sex": "female",
            "weight": 60.0,
            "height": 165.0,
            "phone": "9876543210"
        }
    )
    # Retrieve the patient
    response = client.get("/patients/1")
    assert response.status_code == 200
    assert response.json()["name"] == "Jane Doe"


def test_update_patient(client):
    # Update patient details
    response = client.put(
        "/patients/1",
        json={
            "name": "Lasun Kabiru",
            "age": 26,
            "sex": "male",
            "weight": 62.0,
            "height": 167.0,
            "phone": "08033016569"
        }
    )
    assert response.status_code == 200
    assert response.json()["name"] == "Jane Smith"


def test_delete_patient(client):
    response = client.delete("/patients/1")
    assert response.status_code == 200
    assert response.json()["message"] == "Patient deleted successfully."
