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
