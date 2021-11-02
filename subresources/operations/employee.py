from sqlalchemy.orm import Session
from ..sql_app import sqlModel
from fastapi import Depends

employeeModel = sqlModel.Employee


def update_employee(db, request, id):
    employeeUpdate = db.query(employeeModel).filter(employeeModel.id == id)
    if not employeeUpdate.first():
        return
    employeeUpdate.update(request.dict())
    db.commit()
    return "Update Success"


def delete_employee(db, id):
    db.query(employeeModel).filter(employeeModel.id == id).delete(synchronize_session=False)
    db.commit()
    return "Done"


def read_employee(db,id):
    employee = db.query(employeeModel).filter(employeeModel.id == id).first()
    if not employee:
        return
    return employee

def read_all_employee(db):
    employies =  db.query(employeeModel).all()
    return employies


def create_employee(db, request):
    newEmployee = employeeModel(name = request.name, email = request.email, is_active = request.is_active, hashed_password = request.hashed_password)
    db.add(newEmployee)
    db.commit()
    db.refresh(newEmployee)
    return newEmployee