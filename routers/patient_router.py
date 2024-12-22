from fastapi import APIRouter
from crud.patient_crud import create_patient, list_patients

patient_router = APIRouter()


@patient_router.post("/")
def add_patient(patient):
    return create_patient(patient.dict())


@patient_router.get("/")
def get_all_patients():
    return list_patients()
