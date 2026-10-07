from database.connection import get_connection
from exceptions.employee_exceptions import EmployeeRepositoryError

def fetch_all_employees():

    try:
        with get_connection() as connection : #create the database connection 
            with connection.cursor() as cursor :  #creating the cursor to write the sql 

                query = """ SELECT * FROM employees """

                cursor.execute (query) #Send SQL command to database

                columns = [column.name for column in cursor.description] # get all the column names using description 

                employees_data = cursor.fetchall() #Gets all rows returned by the query

                return columns , employees_data 
            
    except Exception as er :
        raise EmployeeRepositoryError( f"Iusse in repositry : {er}")
    

def post_new_employee(employee):
    try:
        with get_connection() as connection : 
            with connection.cursor() as cursor :  

                query = """ INSERT INTO employees ( 
                            employee_id,
                            employee_name,
                            employee_basic_salary,
                            pf,
                            da,
                            gross_salary) VALUES (%s, %s, %s, %s, %s, %s)  """
                
                values = ( employee["EmployeeId"], employee["EmployeeName"],
                           employee["EmployeeBasicSalary"], employee["PF"],
                           employee["DA"], employee["GrossSalary"])

                cursor.execute(query,values)

                connection.commit()

                return {
                        "message":"Employee Created",
                        "EmployeeId" :employee["EmployeeId"] ,
                        "EmployeeName" : employee["EmployeeName"]
                        }


    except Exception as er:
        raise EmployeeRepositoryError( f"Iusse in repositry : {er}")
            

def delete_employee(employee_id):
    try:
        with get_connection() as connection : 
            with connection.cursor() as cursor :

                query=""" DELETE FROM employees WHERE employee_id = %s"""

                cursor.execute(query,(employee_id,))
 
        
                connection.commit()

                return{
                            "message":"Employee deleted",
                            "EmployeeId" : employee_id
                        }
                
    except Exception as er:
            raise EmployeeRepositoryError( f"Iusse in repositry : {er}")
                
