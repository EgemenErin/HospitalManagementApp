from hospital import Hospital
from doctor import Doctor
from nurse import Nurse
from schedule import Schedule
from administrator import Administrator
from utils import get_employee_details
import datetime

def main():
    hospital = Hospital()
    schedule = Schedule()
    logged_in_user = None

    def login():
        nonlocal logged_in_user
        username = input("Enter username: ")
        password = input("Enter password: ")
        user = hospital.get_employee_by_username(username)
        if user and user.password == password:
            logged_in_user = user
            print(f"Welcome {user.name} ({user.__class__.__name__})!")
        else:
            print("Invalid username or password.")

    def admin_menu():
        while True:
            print("\nAdmin Menu")
            print("1. Add Employee")
            print("2. Check if User Exists")
            print("3. Schedule Appointment")
            print("4. Check Availability")
            print("5. Get Employee Schedule")
            print("6. List Employees")
            print("7. Logout")
            choice = input("Enter your choice: ")

            if choice == "1":
                name = input("Enter name: ")
                surname = input("Enter surname: ")
                pesel_number = input("Enter PESEL number: ")
                username = input("Enter username: ")
                password = input("Enter password: ")
                role = input("Enter role (doctor/nurse): ")

                if role.lower() == "doctor":
                    pwz_number = input("Enter PWZ number: ")
                    specialist = input("Enter specialist: ")
                    new_employee = Doctor(name, surname, pesel_number, username, password, pwz_number, specialist)
                elif role.lower() == "nurse":
                    new_employee = Nurse(name, surname, pesel_number, username, password)
                else:
                    print("Invalid role!")
                    continue

                hospital.add_employee(new_employee)
                print("Employee added successfully!")

            elif choice == "2":
                username = input("Enter username to check: ")
                if hospital.user_exists(username):
                    print("User exists.")
                else:
                    print("User does not exist.")

            elif choice == "3":
                schedule_appointment()

            elif choice == "4":
                check_availability()

            elif choice == "5":
                get_employee_schedule()

            elif choice == "6":
                print("Employees list:")
                for employee in hospital.employees:
                    details = get_employee_details(employee)
                    for key, value in details.items():
                        print(f"{key}: {value}")
                    print()

            elif choice == "7":
                break

            else:
                print("Invalid choice! Please try again.")

    def doctor_menu():
        while True:
            print("\nDoctor Menu")
            print("1. Schedule Appointment")
            print("2. Check Availability")
            print("3. Get Employee Schedule")
            print("4. Logout")
            choice = input("Enter your choice: ")

            if choice == "1":
                schedule_appointment()

            elif choice == "2":
                check_availability()

            elif choice == "3":
                get_employee_schedule()

            elif choice == "4":
                break

            else:
                print("Invalid choice! Please try again.")

    def schedule_appointment():
        username = input("Enter username: ")
        employee = hospital.get_employee_by_username(username)
        if not employee:
            print("Employee not found!")
            return

        date_str = input("Enter appointment date (YYYY-MM-DD): ")
        date = datetime.datetime.strptime(date_str, "%Y-%m-%d")
        try:
            schedule.add_appointment(date, employee)
            print("Appointment scheduled successfully!")
        except Exception as e:
            print(e)

    def check_availability():
        username = input("Enter username: ")
        employee = hospital.get_employee_by_username(username)
        if not employee:
            print("Employee not found!")
            return

        date_str = input("Enter date to check (YYYY-MM-DD): ")
        date = datetime.datetime.strptime(date_str, "%Y-%m-%d")
        if schedule.is_available(date, employee):
            print("Employee is available.")
        else:
            print("Employee is not available.")

    def get_employee_schedule():
        username = input("Enter username: ")
        employee = hospital.get_employee_by_username(username)
        if not employee:
            print("Employee not found!")
            return

        employee_schedule = schedule.get_schedule(employee)
        print(f"Schedule for {username}:")
        for appt_date in employee_schedule:
            print(appt_date)

    while True:
        print("Hospital Management System")
        print("1. Login")
        print("2. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            login()
            if isinstance(logged_in_user, Administrator):
                admin_menu()
            elif isinstance(logged_in_user, Doctor):
                doctor_menu()
            else:
                print("Access denied. Only administrators and doctors can log in.")
        elif choice == "2":
            break
        else:
            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    main()
