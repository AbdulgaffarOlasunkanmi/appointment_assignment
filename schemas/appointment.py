from pydantic import BaseModel
from datetime import datetime


class AppointmentBase(BaseModel):
    patient_id: int
    doctor_id: int
    date: datetime


class AppointmentCreate(BaseModel):
    patient_id: int
    date: datetime


class AppointmentResponse(AppointmentBase):
    id: int
