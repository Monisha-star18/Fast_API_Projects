from repositories.employee_repository import fetch_all_employees , post_new_employee , delete_employee 
from .payroll_service import PayrollService

def get_all_employees() :

    columns ,employees_data  = fetch_all_employees()

    employees = []

    for employee in employees_data :

        employee_data = dict(zip(columns,employee))
        employees.append(employee_data)

    return employees

def create_employee(employee_data):

    basic_salary = employee_data.EmployeeBasicSalary

    da = PayrollService.calculate_da(basic_salary)
    pf = PayrollService.calculate_pf(basic_salary)
    gross_salary = PayrollService.calculate_gross_salary(basic_salary)

    employee = {
        "EmployeeId": employee_data.EmployeeId,
        "EmployeeName": employee_data.EmployeeName,
        "EmployeeBasicSalary": basic_salary,
        "PF": pf,
        "DA": da,
        "GrossSalary": gross_salary
    }

    return post_new_employee(employee)


def remove_employee_byid(employee_id):

    return delete_employee(employee_id)
