patients = []


def create_patient(patient):
    patient["id"] = len(patients) + 1
    patients.append(patient)
    return patient


def get_patient_by_id(patient_id):
    return next((p for p in patients if p["id"] == patient_id), None)


def delete_patient(patient_id):
    patient = get_patient_by_id(patient_id)
    if patient:
        patients.remove(patient)
        return True
    return False


def list_patients():
    return patients
