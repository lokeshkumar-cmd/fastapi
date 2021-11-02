from sqlalchemy.orm import Session
from ..sql_app import sqlModel
from fastapi import Depends

employerModel = sqlModel.Employer


def update_employer(db, request, id):
    employerUpdate = db.query(employerModel).filter(employerModel.id == id)
    if not employerUpdate.first():
        return
    employerUpdate.update(request.dict())
    db.commit()
    return "Update Success"


def delete_employer(db, id):
    db.query(employerModel).filter(employerModel.id == id).delete(synchronize_session=False)
    db.commit()
    return "Done"


def read_employer(db,id):
    employer = db.query(employerModel).filter(employerModel.id == id).first()
    if not employer:
        return
    return employer

def read_all_employer(db):
    employers =  db.query(employerModel).all()
    return employers


def create_employer(db, request):
    newEmployer = employerModel(name = request.name, email = request.email, is_active = request.is_active, hashed_password = request.hashed_password)
    db.add(newEmployer)
    db.commit()
    db.refresh(newEmployer)
    return newEmployer