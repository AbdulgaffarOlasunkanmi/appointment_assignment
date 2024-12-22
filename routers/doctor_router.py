from fastapi import APIRouter
from crud.doctor_crud import create_doctor, get_available_doctor
# set_doctor_availability

doctor_router = APIRouter()


@doctor_router.post("/")
def add_doctor(doctor):
    return create_doctor(doctor.dict())


@doctor_router.get("/available")
def get_available():
    return get_available_doctor()
