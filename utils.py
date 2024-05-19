def get_employee_details(employee):
    return {
        'Name': employee.name,
        'Surname': employee.surname,
        'PESEL Number': employee.pesel_number,
        'Username': employee.username
    }
