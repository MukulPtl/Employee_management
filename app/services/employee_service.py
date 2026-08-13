from app.repositories.employee_repository import EmployeeRepository

class EmployeeService:

    def __init__(self):
        self.repository = EmployeeRepository()

    def create_employee(self, employee):
        saved_employee = self.repository.save(employee)
        return {
            "message": "Employee created successfully",
            "employee": saved_employee
        }

    def get_employee(self):
        return {
            "employees": [
                        {
                            "id": 1,
                            "name": "Mukul",
                            "department": "Engineering"
                        },
                        {
                            "id": 2,
                            "name": "Alice",
                            "department": "HR"
                        },
                        {
                            "id": 3,
                            "name": "Mohan",
                            "department": "Finance"
                        }
                    ]
        }

    def get_department(self):
        return {
            "departments": [
                        "Engineering",
                        "HR",
                        "Finance"
                    ]
        }