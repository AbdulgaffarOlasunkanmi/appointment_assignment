from fastapi import FastAPI
from routers.patient_router import patient_router
from routers.doctor_router import doctor_router
from routers.appointment_router import appointment_router

app = FastAPI()

app.include_router(patient_router, prefix="/patients", tags=["Patients"])
app.include_router(doctor_router, prefix="/doctors", tags=["Doctors"])
app.include_router(appointment_router,
                   prefix="/appointments", tags=["Appointments"])


# @app.get("/")
# def home():
# return {"message": "Welcome to the Medical Appointment"}
