from employee import Employee
import datetime

class MedicalStaff(Employee):
    def __init__(self, name, surname, pesel_number, username, password):
        super().__init__(name, surname, pesel_number, username, password)
        self._on_call_duty = []

    @property
    def on_call_duty(self):
        return self._on_call_duty

    @on_call_duty.setter
    def on_call_duty(self, duty_list):
        self._on_call_duty = duty_list

    def update(self, n, s, p, u, pa, hospital):
        super().update(n, s, p, u, pa, hospital)

    def remove_duty(self, date):
        if date in self._on_call_duty:
            self._on_call_duty.remove(date)

    def add_duty(self, date):
        if self.check_duty_in_month(date):
            if self.duty_day_check(date) and not self.duty_exists(date):
                self._on_call_duty.append(date)

    def duty_exists(self, date):
        return date in self._on_call_duty

    def duty_day_check(self, date):
        for duty_date in self._on_call_duty:
            if date == duty_date + datetime.timedelta(days=1) or date == duty_date - datetime.timedelta(days=1):
                raise Exception("Cannot add duty adjacent to another duty")
            if date == duty_date:
                raise Exception("Cannot add a duty that already exists")
        return True

    def check_duty_in_month(self, date):
        month_duties = [d for d in self._on_call_duty if d.month == date.month and d.year == date.year]
        if len(month_duties) >= 10:
            raise Exception("Amount of duties for this month is above 10")
        return True
