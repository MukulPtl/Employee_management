# Project_Design

## Project

Employee Management Backend

The Employee Management Backend is the central project used throughout the backend engineering roadmap.

---

## Current Stack

- Python 3.12
- FastAPI
- PostgreSQL
- pgAdmin 4
- Docker
- Git
- WSL2

### Planned/Upcoming

- SQLAlchemy
- psycopg
- Database connection pooling
- Database sessions

---

## Current Structure

```text
.
├── README.md
├── app
│   ├── __pycache__
│   │   ├── __init__.cpython-312.pyc
│   │   ├── main.cpython-312.pyc
│   │   └── schemas.cpython-312.pyc
│   ├── database.py
│   ├── main.py
│   ├── models
│   │   └── __init__.py
│   ├── repositories
│   │   ├── __init__.py
│   │   ├── __pycache__
│   │   │   ├── __init__.cpython-312.pyc
│   │   │   └── employee_repository.cpython-312.pyc
│   │   └── employee_repository.py
│   ├── routes
│   │   ├── __init__.py
│   │   ├── __pycache__
│   │   │   ├── __init__.cpython-312.pyc
│   │   │   └── employee_routes.cpython-312.pyc
│   │   └── employee_routes.py
│   ├── schemas.py
│   └── services
│       ├── __init__.py
│       ├── __pycache__
│       │   ├── __init__.cpython-312.pyc
│       │   └── employee_service.cpython-312.pyc
│       └── employee_service.py
├── docs
│   ├── Lesson_Tracker.md
│   ├── Master_Roadmap.md
│   └── Project_Design.md
├── requirements.txt
└── tests
```
---

## PostgreSQL Integration Status

### PostgreSQL Setup

- PostgreSQL 18 installed on Windows.
- PostgreSQL service: `postgresql-x64-18`
- Database created: `employee_management`
- PostgreSQL port: `5432`
- `listen_addresses = *`

### Application Environment

The Employee Management Backend runs inside WSL2.

Current conceptual architecture:

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

### Current Database Integration

PostgreSQL has been installed and the database has been created, but the application has not yet been integrated with PostgreSQL.

The WSL2 application currently cannot reach the Windows PostgreSQL server on port `5432`.

No firewall or security settings have been changed to resolve this.

The current repository implementation remains the existing in-memory implementation.

### Database Concepts Learned

- PostgreSQL as a DBMS
- Persistent storage
- PostgreSQL server vs FastAPI application
- Database ports
- pgAdmin vs PostgreSQL server
- Database connection
- `psycopg`
- Connection object
- Cursor
- `execute()`
- `fetchone()`

### Next Step

Continue learning PostgreSQL fundamentals by understanding:

1. Tables
2. Rows
3. Columns
4. Designing the `employees` table

Database integration into the repository will happen after the underlying database concepts are understood.

---