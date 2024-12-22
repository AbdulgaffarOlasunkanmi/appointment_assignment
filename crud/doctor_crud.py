doctors = []


def create_doctor(doctor):
    doctor["id"] = len(doctors) + 1
    doctor["is_available"] = True
    doctors.append(doctor)
    return doctor


def get_available_doctor():
    return next((d for d in doctors if d["is_available"]), None)


def set_doctor_availability(doctor_id, is_available):
    doctor = next((d for d in doctors if d["id"] == doctor_id), None)
    if doctor:
        doctor["is_available"] = is_available
        return doctor
    return None
