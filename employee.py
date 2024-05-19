class Employee:
    def __init__(self, name, surname, pesel_number, username, password):
        self._name = name
        self._surname = surname
        self._pesel_number = pesel_number
        self._username = username
        self._password = password

    @property
    def name(self):
        return self._name

    @property
    def surname(self):
        return self._surname

    @property
    def pesel_number(self):
        return self._pesel_number

    @property
    def username(self):
        return self._username

    @property
    def password(self):
        return self._password

    def update(self, n, s, p, u, pa, hospital):
        if not n:
            raise ValueError("Name is empty")
        if not s:
            raise ValueError("Surname is empty")
        if not p:
            raise ValueError("PESELNumber is empty")
        if not u:
            raise ValueError("Username is empty")
        if not pa:
            raise ValueError("Password is empty")

        if u != self._username and hospital.user_exists(u):
            raise ValueError("Username already exists")

        self._name = n
        self._surname = s
        self._pesel_number = p
        self._username = u
        self._password = pa
