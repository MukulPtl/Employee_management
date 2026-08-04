from fastapi import FastAPI
from app.schemas import EmployeeCreate

application = FastAPI()

@application.get("/")
def root():
    return {"Message":"Employee Management Backend is running!"}

@application.get("/employees")
def get_employees():
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
                "id":3,
                "name": "Mohan",
                "department":"Finance"
            }
        ]
    }


@application.get("/departments")
def get_departments():
    return {
        "departments": [
            "Engineering",
            "HR",
            "Finance"
        ]
    }


@application.post("/employees")
def create_employee(employee: EmployeeCreate):
    return {
        "message": "Employee created successfully",
        "employee": employee
    }

@application.post("/test")
def test(employee: EmployeeCreate):
    print(type(employee))
    print(employee)

    return {"message": "Done"}