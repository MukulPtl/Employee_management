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
        return self.repository.get_all()

    def get_department(self):
        return self.repository.get_all_department()