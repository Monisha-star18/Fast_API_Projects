# Employee Payroll Management API

A simple REST API built with **FastAPI** and **PostgreSQL** to manage employees and calculate their salary components (DA, PF and gross salary).

## Tech Stack

- Python 3.14
- FastAPI
- Uvicorn
- PostgreSQL
- psycopg 3
- Pydantic v2
- python-dotenv

## Project Structure

```
payroll_management/

|
├── database/
│   └── connection.py            # PostgreSQL connection
├── models/
│   └── employee_model.py        # Request validation (Pydantic)
├── routers/
│   └── employee_router.py       # API endpoints
├── services/
│   ├── employee_service.py      # Business logic
│   └── payroll_service.py       # DA, PF, gross salary calculations
├── repositories/
│   └── employee_repository.py   # SQL queries
├── exceptions/
│   └── employee_exceptions.py   # Custom exceptions
|
├── requirements.txt
└── .env                         # Database credentials (not committed)
├── main.py                      # App entry point
├── config.py                    # Loads settings from .env
```

## Setup

### 1. Clone and create a virtual environment

```bash

python -m venv .venv

```

```bash

.venv\Scripts\activate        # Windows

```

### 2. Install dependencies

```bash

pip install -r requirements.txt

```

### 3. Create the database

```sql

CREATE DATABASE payroll_db;

CREATE TABLE employees (
    employee_id            INTEGER        PRIMARY KEY CHECK (employee_id > 0),
    employee_name          VARCHAR(100)   NOT NULL,
    employee_basic_salary  NUMERIC(12,2)  NOT NULL CHECK (employee_basic_salary >= 5000),
    pf                     NUMERIC(12,2)  NOT NULL,
    da                     NUMERIC(12,2)  NOT NULL,
    gross_salary           NUMERIC(12,2)  NOT NULL
);

```

### 4. Configure environment variables

Create a `.env` file in the project root:

```
DB_HOST=localhost
DB_PORT=5432
DB_NAME=payroll_db
DB_USER=postgres
DB_PASSWORD=your_password

```

### 5. Run the server

```bash

uvicorn main:app --reload

```

The API runs at `http://127.0.0.1:8000`.
Interactive docs (Swagger UI): `http://127.0.0.1:8000/docs`

## API Endpoints

| Method | Endpoint                    | Description              |
|--------|-----------------------------|--------------------------|
| GET    | `/api/employees/`           | Get all employees        |
| POST   | `/api/employees/`           | Create a new employee    |
| DELETE | `/api/employees/{employee_id}` | Delete an employee    |

### Create employee: example request

`POST /api/employees/`

```json
{
  "EmployeeId": 1,
  "EmployeeName": "Arun",
  "EmployeeBasicSalary": 20000
}
```

### Response

```json
{
  "message": "Employee Created",
  "EmployeeId": 1,
  "EmployeeName": "Arun"
}
```

### Delete employee: example

`DELETE /api/employees/1`

```json
{
  "message": "Employee deleted",
  "EmployeeId": 1
}
```

## Validation Rules

- `EmployeeId`: integer greater than 0
- `EmployeeName`: 3 to 100 characters, letters only
- `EmployeeBasicSalary`: from 5,000 up to (but not including) 1,000,000
- Extra fields in the request body are rejected

## Notes

- Never commit your `.env` file. Add it and `.venv/` to `.gitignore`.
- deactivate to end .venv session