# Lesson_Tracker

## Completed Lessons

1. Virtual Environments, Git, Project Structure
2. Backend Architecture
3. HTTP
4. FastAPI Routes
5. Pydantic & Validation
6. Layered Architecture (Route, Service, Repository, Database)
7. Python Modules, Packages & Imports
8. Employee Management Backend Layered Refactoring
9. PostgreSQL Fundamentals & Database Setup

---

## Lesson 8: Employee Management Backend Layered Refactoring

### Completed

- Created production-style application structure.
- Created:
  - `app/routes/`
  - `app/services/`
  - `app/repositories/`
  - `app/models/`
- Moved employee-related API routes from `main.py` to:
  - `app/routes/employee_routes.py`
- Introduced `APIRouter`.
- Updated `main.py` to register the employee router using `include_router()`.
- Removed the temporary `/test` endpoint.
- Verified:
  - `GET /`
  - `GET /employees`
  - `GET /departments`
  - `POST /employees`
  - `/docs`
- Introduced `EmployeeService`.
- Moved employee creation logic from the route into `EmployeeService.create_employee()`.
- Introduced `EmployeeRepository`.
- Connected `EmployeeService` to `EmployeeRepository`.
- Implemented temporary in-memory repository behavior.
- Refactored `GET /employees` through:
  - Route
  - Service
  - Repository
- Verified the refactored application continues to work.

### Architecture Understanding

```text
Route
  ↓
Service
  ↓
Repository
  ↓
Database