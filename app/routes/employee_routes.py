from fastapi import APIRouter
from app.services.employee_service import EmployeeService
from app.schemas import EmployeeCreate

router = APIRouter()
employee_service = EmployeeService()

@router.get("/employees")
def get_employees():
    return employee_service.get_employee()


@router.get("/departments")
def get_departments():
    return employee_service.get_department()


@router.post("/employees")
def create_employee(employee: EmployeeCreate):
    return employee_service.create_employee(employee)