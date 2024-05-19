from employee import Employee

class Administrator(Employee):
    def __init__(self, name, surname, pesel_number, username, password):
        super().__init__(name, surname, pesel_number, username, password)
