import datetime

class Schedule:
    def __init__(self):
        self._appointments = []

    def add_appointment(self, date, employee):
        if not self.is_available(date, employee):
            raise Exception("Employee is not available at this time")
        self._appointments.append((date, employee))

    def remove_appointment(self, date, employee):
        self._appointments = [appt for appt in self._appointments if appt != (date, employee)]

    def is_available(self, date, employee):
        for appt_date, appt_employee in self._appointments:
            if appt_employee == employee and appt_date == date:
                return False
        return True

    def get_schedule(self, employee):
        return [appt_date for appt_date, appt_employee in self._appointments if appt_employee == employee]
