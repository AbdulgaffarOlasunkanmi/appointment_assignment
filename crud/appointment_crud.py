appointments = []


def create_appointment(appointment):
    appointment["id"] = len(appointments) + 1
    appointments.append(appointment)
    return appointment


def delete_appointment(appointment_id):
    appointment = next(
        (a for a in appointments if a["id"] == appointment_id), None)
    if appointment:
        appointments.remove(appointment)
        return True
    return False


def list_appointments():
    return appointments
