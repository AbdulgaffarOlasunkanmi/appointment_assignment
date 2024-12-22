from crud.doctor_crud import get_available_doctor, set_doctor_availability
from crud.appointment_crud import create_appointment


def create_appointment_service(appointment_data):
    doctor = get_available_doctor()
    if not doctor:
        return {"error": "No doctors are available"}

    appointment_data["doctor_id"] = doctor["id"]
    set_doctor_availability(doctor["id"], False)
    return create_appointment(appointment_data)
