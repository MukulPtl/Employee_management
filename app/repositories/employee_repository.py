# app/repositories/employee_repository.py

class EmployeeRepository:

    def save(self, employee):
        return employee
    
    def get_all(self):
        return [
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

    def get_all_department(self):
        return {
            "departments": [
                        "Engineering",
                        "HR",
                        "Finance"
                    ]
        } 