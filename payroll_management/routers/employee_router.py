from fastapi import APIRouter,Path

from services.employee_service import get_all_employees , create_employee , remove_employee_byid
from models.employee_model import CreateEmployee

router = APIRouter( prefix="/api/employees")


#get employees and salary deatils
@router.get("/")
def get_employees():
    
    employees = get_all_employees()

    return employees

#post the detailes 
@router.post("/")
def create_new_employee(employee_data : CreateEmployee):

    employee_details = create_employee(employee_data)

    return employee_details

#delect an employee
@router.delete('/{employee_id}')
def remove_employee(employee_id : int =Path(gt=0) ):

    return remove_employee_byid(employee_id)