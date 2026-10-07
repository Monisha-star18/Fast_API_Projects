to create the virtual environment 

python -m venv .venv
.venv\Scripts\activate
python -m pip install fastapi "uvicorn[standard]" psycopg[binary] python-dotenv


DB_HOST = localhost
DB_PORT = 5432
DB_NAME = payroll_db
DB_USER = postgres 
DB_PASSWORD = 