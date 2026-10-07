from pydantic import BaseModel , Field , field_validator , ConfigDict

class CreateEmployee(BaseModel) :

    model_config = ConfigDict(extra='forbid')

    EmployeeId   : int = Field(gt=0)
    EmployeeName : str = Field(min_length=3, max_length=100)
    EmployeeBasicSalary : float = Field(ge=5_000,lt=1_000_000)

    @field_validator("EmployeeName")
    @classmethod
    def name_validator(cls,name):

        if name == "string":
            raise ValueError("Fill the employee name")
        if not name.isalpha() :
            raise ValueError("Name should contain only letter not numbers")

        return name
    



