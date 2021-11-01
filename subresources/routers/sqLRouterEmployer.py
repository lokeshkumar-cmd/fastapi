from typing import List
from fastapi import APIRouter , Depends, HTTPException, status, Response
from ..sql_app import database, sqlModel, sqlSchema
from sqlalchemy.orm import Session

router = APIRouter()

get_db = database.get_db 

@router.post('/sqlDatabase/employer/creates', status_code = status.HTTP_201_CREATED, tags = ['Employer'])
def sql_database_create_employee(employer: sqlSchema.Employer, db: Session = Depends(get_db)):
    newEmployer = sqlModel.Employer(name = employer.name, email = employer.email, is_active = employer.is_active, employee_id = employer.employee_id)
    db.add(newEmployer)
    db.commit()
    db.refresh(newEmployer)
    return newEmployer 


@router.get('/sqlDatabase/employer/info', response_model = List[sqlSchema.ShowEmployer], tags = ['Employer'])
async def all(db: Session = Depends(get_db)):
    employers = db.query(sqlModel.Employer).all()
    return employers


@router.get('/sqlDatabase/employer/singleinfo/{id}', response_model = sqlSchema.ShowEmployer, tags = ['Employer']) # , response_model_exclude_unset=True, response_model_exclude={"reLEmployee"}
async def single_info_employer(id,response: Response, db: Session = Depends(database.get_db)):
    try:
        employer = db.query(sqlModel.Employer).filter(sqlModel.Employer.id == id).first()
    except Exception as e:
        return dict('error', e)
    if not employer:
       raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = {"error": f'details not found for id {id}'}) 
    return employer


@router.put('/sqlDatabase/employer/update/{id}', status_code = status.HTTP_202_ACCEPTED, tags = ['Employer'])
async def update(id, response: Response, employer: sqlSchema.Employer, db: Session = Depends(get_db)):
    employerUpdate = db.query(sqlModel.Employer).filter(sqlModel.Employer.id == id).update(employer.dict())
    print(employerUpdate)
    if not employerUpdate:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail ={'error': f'no details found for id {id}'})
    db.commit()
    return 'Updated success'


@router.delete('/sqlDatabase/employer/delete/{id}', status_code = status.HTTP_204_NO_CONTENT, tags = ['Employer'])
def drop(id, db: Session = Depends(database.get_db)):
    db.query(sqlModel.Employer).filter(sqlModel.Employer.id == id).delete(synchronize_session=False)
    db.commit()
    return "Done"

