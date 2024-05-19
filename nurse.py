from medical_staff import MedicalStaff

class Nurse(MedicalStaff):
    def __init__(self, name, surname, pesel_number, username, password):
        super().__init__(name, surname, pesel_number, username, password)
