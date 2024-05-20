
# Hospital Management System

This project is a Python implementation of a Hospital Management System. The system includes functionality to manage hospital employees and ensure data integrity by checking for unique usernames and validating input data.

## Project Structure

- `hospital.py`: Contains the `Hospital` class definition.
- `employee.py`: Contains the `Employee` class definition.

## Features

- Add and manage hospital employees.
- Validate employee data to ensure no fields are empty.
- Check for unique usernames within the hospital system.
- Update employee details with proper validation.

## Setup

### Prerequisites

- Python 3.6 or higher

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/hospital-management-system.git
   ```

2. Navigate to the project directory:

   ```bash
   cd hospital-management-system
   ```

## Usage

1. Ensure you have the necessary files:

   - `hospital.py`
   - `employee.py`

2. Create a script (e.g., `main.py`) to utilize the classes:

   ```python
   from hospital import Hospital
   from employee import Employee

   # Initialize the hospital
   hospital = Hospital()

   # Add a new employee
   employee = Employee("John", "Doe", "12345678901", "johndoe", "password123")
   hospital.users[employee.username] = employee

   # Update employee details
   try:
       employee.update("Jane", "Doe", "10987654321", "janedoe", "newpassword123", hospital)
   except ValueError as e:
       print(e)

   # Print updated employee details
   print(vars(employee))
   ```

3. Run your script:

   ```bash
   python main.py
   ```

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/YourFeature`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature/YourFeature`).
5. Open a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
