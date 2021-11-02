from typing import List
from fastapi import APIRouter , Depends, HTTPException, status, Response
from ..sql_app import database, sqlModel, sqlSchema
from sqlalchemy.orm import Session
from ..operations.employer import create_employer, update_employer, delete_employer, read_all_employer, read_employer

router = APIRouter(
    prefix  = "/sqlDatabase/Employer",
    tags = ['Employer']
)

get_db = database.get_db 

@router.post('/creates', status_code = status.HTTP_201_CREATED)
def sql_database_create_employee(employer: sqlSchema.Employer, db: Session = Depends(get_db)):
    return create_employer(db, employer)


@router.get('/info', response_model = List[sqlSchema.ShowEmployer])
async def all(db: Session = Depends(get_db)):
    return read_all_employer(db)


@router.get('/singleinfo/{id}', response_model = sqlSchema.ShowEmployer) # , response_model_exclude_unset=True, response_model_exclude={"reLEmployee"}
async def single_info_employer(id,response: Response, db: Session = Depends(database.get_db)):
    employer = read_employer(db, id)
    if not employer:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = {"error": f'details not found for id {id}'}) 
    return employer


@router.put('/update/{id}', status_code = status.HTTP_202_ACCEPTED)
async def update(id, response: Response, employer: sqlSchema.Employer, db: Session = Depends(get_db)):
    employerUpdate = update_employer(db, employer, id)
    if not employerUpdate:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail ={'error': f'no details found for id {id}'})
    return 'Updated success'


@router.delete('/delete/{id}', status_code = status.HTTP_204_NO_CONTENT)
def drop(id, db: Session = Depends(database.get_db)):
    return delete_employer(db, id)

