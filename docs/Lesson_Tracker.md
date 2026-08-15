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

## Lesson 9 — PostgreSQL Fundamentals and Database Connection

### Concepts Covered

- PostgreSQL is a Database Management System (DBMS).
- A database provides persistent storage for application data.
- Difference between temporary in-memory application data and persistent database data.
- PostgreSQL runs separately from the FastAPI application.
- FastAPI and PostgreSQL are separate processes/services.
- FastAPI commonly listens on port `8000`.
- PostgreSQL commonly listens on port `5432`.
- Understanding that an application can listen for client requests on one port while making an outgoing connection to another service on a different port.
- pgAdmin is a GUI/client tool used to interact with PostgreSQL.
- pgAdmin is not part of the runtime communication path between FastAPI and PostgreSQL.
- The application communicates with PostgreSQL directly.
- Basic PostgreSQL connection parameters:
  - Host
  - Port
  - Database name
  - Username
  - Password
- `psycopg` is a Python PostgreSQL driver.
- `psycopg.connect()` is used to establish a database connection.
- A connection object represents the established communication with PostgreSQL.
- A cursor is a separate object created from a connection.
- A cursor is used to execute SQL and retrieve query results.
- `cursor.execute()` executes SQL through the database connection.
- `cursor.fetchone()` retrieves one row from the query result.
- `SELECT 1` returns `(1,)` because the result consists of one row containing one column.

### Architecture Understanding

Current conceptual flow:

Client
  ↓ HTTP
FastAPI
  ↓
Routes
  ↓
Services
  ↓
Repositories
  ↓
PostgreSQL

Database interaction at the lower level:

Python
  ↓
psycopg
  ↓
Connection
  ↓
Cursor
  ↓
SQL
  ↓
PostgreSQL
  ↓
Result

### PostgreSQL Environment

- PostgreSQL 18 is installed on Windows.
- PostgreSQL service `postgresql-x64-18` is running.
- Database `employee_management` was created.
- PostgreSQL was verified to be listening on port `5432`.
- PostgreSQL `listen_addresses` was verified as `*`.
- Windows can connect to PostgreSQL on port `5432`.
- The Employee Management Backend runs inside WSL2.
- WSL currently cannot reach the Windows PostgreSQL server on port `5432`.

### Environment Issue

The WSL → Windows PostgreSQL connectivity issue was investigated.

No firewall or security settings were changed.

The issue is intentionally not being solved by weakening firewall/security configuration.

The primary objective is learning the backend/database concepts, not forcing the current development environment to work at the cost of system security.

### Current Learning State

The concept of PostgreSQL tables has been introduced but has NOT yet been completed.

The next lesson should continue with:

- What a PostgreSQL table represents
- Rows
- Columns
- Persistence compared with Python in-memory data
- Designing the `employees` table

Do not jump directly to SQLAlchemy.

### Not Yet Covered

- Creating the `employees` table
- `CREATE TABLE`
- `INSERT`
- `SELECT` against employee data
- `UPDATE`
- `DELETE`
- Integrating PostgreSQL into `EmployeeRepository`
- SQLAlchemy
- Database sessions
- Connection pooling

### Architecture Understanding

```text
Route
  ↓
Service
  ↓
Repository
  ↓
Database