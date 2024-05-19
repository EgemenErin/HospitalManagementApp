from administrator import Administrator
from doctor import Doctor
from nurse import Nurse

class Hospital:
    def __init__(self):
        self._employees = [
            Administrator("Eric", "Muganga", "0234456750", "admin", "admin"),
            Doctor("Derek", "Gisa", "303094499", "derek", "derek", "12304", "Cardiologist")
        ]

    @property
    def employees(self):
        return self._employees

    @employees.setter
    def employees(self, value):
        self._employees = value

    def add_employee(self, employee):
        self._employees.append(employee)

    def user_exists(self, username):
        for empl in self._employees:
            if empl.username == username:
                return True
        return False

    def get_employee_by_username(self, username):
        for empl in self._employees:
            if empl.username == username:
                return empl
        return None
