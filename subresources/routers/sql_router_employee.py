from fastapi import APIRouter , Depends, HTTPException, status, Response
from ..sql_app import database, sqlModel, sqlSchema
from sqlalchemy.orm import Session

router = APIRouter()

get_db = database.get_db 


@router.post('/sqlDatabase/employee/create', status_code = 201)
def sql_database_create_employee(employee: sqlSchema.Employee, db: Session = Depends(database.get_db)):
    newEmployee = sqlModel.Employee(name = employee.name, email = employee.email, is_active = employee.is_active, hashed_password = employee.hashed_password)
    db.add(newEmployee)
    db.commit()
    db.refresh(newEmployee)
    return newEmployee


@router.get('/sqlDatabase/employee/info', status_code = 200)
def all(db: Session = Depends(get_db)):
    employies =  db.query(sqlModel.Employee).all()
    return employies


@router.get('/sqlDatabase/employee/singleinfo/{id}')
async def single_info_employee(id,response: Response, db: Session = Depends(database.get_db)):
    employee = db.query(sqlModel.Employee).filter(sqlModel.Employee.id == id).first()
    if not employee:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {'error': f'details not found for id {id}'}
    return employee


@router.put('/sqlDatabase/employee/update/{id}', status_code = status.HTTP_202_ACCEPTED)
def update(id, response: Response, employee: sqlSchema.Employee, db: Session = Depends(get_db)):
    employee = db.query(sqlModel.Employee).filter(sqlModel.Employee.id == id).update(employee, synchronize_session=False)
    if not employee:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail ={'error': f'no details found for id {id}'})
    db.commit()
    return 'Updated success'


@router.delete('/sqlDatabase/employee/delete/{id}', status_code = status.HTTP_204_NO_CONTENT)
def drop(id, db: Session = Depends(database.get_db)):
    db.query(sqlModel.Employee).filter(sqlModel.Employee.id == id).delete(synchronize_session=False)
    db.commit()
    return "Done"