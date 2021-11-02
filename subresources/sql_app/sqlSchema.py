from typing import Optional
from pydantic import BaseModel

class Employee(BaseModel):
    name: str
    email: str
    hashed_password: str
    is_active: bool = True


class Show_Employee(BaseModel):
    name : str
    email: str
    is_active: bool


    class Config():
        orm_mode = True


class Employer(BaseModel):
    name: str
    email: str
    employee_id: Optional[int]
    is_active: bool = True


class ShowEmployer(BaseModel):
    name: str
    email: str
    is_active: bool
    employee: Show_Employee
    
    
    
    class Config():
        orm_mode = True


class ShowOnlyEmployer(BaseModel):
    id: int
    name: str
    email: str
    is_active: bool
