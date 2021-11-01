from pydantic import BaseModel

class Employee(BaseModel):
    name: str
    email: str
    hashed_password: str
    is_active: bool = True

class Employer(BaseModel):
    name: str
    email: str
    is_active: bool = True
