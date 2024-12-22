from crud.doctor_crud import (
    create_doctor,
    get_doctor_by_id,
    list_doctors,
    set_doctor_availability, get_available_doctor
)
from schemas.doctor import DoctorCreate


def create_doctor_service(doctor_data: DoctorCreate):
    return create_doctor(doctor_data.dict())


def list_doctors_service():
    return list_doctors()


def get_doctor_service(doctor_id: int):
    doctor = get_doctor_by_id(doctor_id)
    if not doctor:
        raise ValueError(f"Doctor with ID {doctor_id} not found.")
    return doctor


def set_availability_service(doctor_id: int, is_available: bool):
    doctor = set_doctor_availability(doctor_id, is_available)
    if not doctor:
        raise ValueError(f"Doctor with ID {doctor_id} not found.")
    return doctor
