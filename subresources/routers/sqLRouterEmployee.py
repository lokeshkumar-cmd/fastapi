from typing import List
from fastapi import APIRouter , Depends, HTTPException, status, Response
from sqlalchemy.orm import Session
from ..sql_app import database, sqlModel, sqlSchema
from .. operations.employee import create_employee, read_all_employee, read_employee, update_employee, delete_employee

router = APIRouter(
    prefix  = "/sqlDatabase/Employee",
    tags = ['Employee']
)

get_db = database.get_db 


@router.post('/create', status_code = 201)
def sql_database_create_employee(employee: sqlSchema.Employee, db: Session = Depends(database.get_db)):
    return create_employee(db, employee)


@router.get('/info',response_model = List[sqlSchema.Show_Employee], status_code = 200)
def all(db: Session = Depends(get_db)):
    return read_all_employee(db)


@router.get('/singleinfo/{id}', response_model = sqlSchema.Show_Employee, status_code = 200)
async def single_info_employee(id,response: Response, db: Session = Depends(database.get_db)):
    employee = read_employee(db, id)
    if not employee:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail ={'error': f'no details found for id {id}'})
    return employee


@router.put('/update/{id}', status_code = status.HTTP_202_ACCEPTED)
def update(id, response: Response, employee: sqlSchema.Employee, db: Session = Depends(get_db)):
    employeeUpdate = update_employee(db, employee, id)
    if not employeeUpdate:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail ={'error': f'no details found for id {id}'})
    return employeeUpdate


@router.delete('/delete/{id}', status_code = status.HTTP_204_NO_CONTENT)
def drop(id, db: Session = Depends(database.get_db)):
    return delete_employee(db, id)