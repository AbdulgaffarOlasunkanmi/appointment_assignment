from fastapi import APIRouter
from services.appointments_service import create_appointment_service

appointment_router = APIRouter()


@appointment_router.post("/")
def schedule_appointment(appointment):
    return create_appointment_service(appointment.dict())
