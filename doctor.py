from medical_staff import MedicalStaff


class Doctor(MedicalStaff):
    def __init__(self, name, surname, pesel_number, username, password, pwz_number, specialist):
        super().__init__(name, surname, pesel_number, username, password)
        self._pwz_number = pwz_number
        self._specialist = specialist

    @property
    def pwz_number(self):
        return self._pwz_number

    @property
    def specialist(self):
        return self._specialist

    def update(self, n, s, p, u, pa, pwz, spec, hospital):
        super().update(n, s, p, u, pa, hospital)
        if not pwz:
            raise ValueError("PWZNumber is empty")
        if not spec:
            raise ValueError("Specialist is empty")

        self._pwz_number = pwz
        self._specialist = spec
