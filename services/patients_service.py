from crud.patient_crud import (create_patient,
                               get_patient_by_id,
                               delete_patient,
                               list_patients)

from schemas.patient import PatientCreate


def create_patient_service(patient_data: PatientCreate):
    return create_patient(patient_data.dict())


def list_patients_service():
    return list_patients()


def get_patient_service(patient_id: int):
    patient = get_patient_by_id(patient_id)
    if not patient:
        raise ValueError(f"Patient with ID {patient_id} not found.")
    return patient


def delete_patient_service(patient_id: int):
    if not delete_patient(patient_id):
        raise ValueError(f"Patient with ID {patient_id} does not exist.")
    return {"message": "Patient deleted successfully."}
