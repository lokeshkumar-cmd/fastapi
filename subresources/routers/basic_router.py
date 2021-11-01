from typing import Optional, List
from fastapi import APIRouter, Depends, HTTPException, status, Response, Query, Path
from .. import functions, schemas

router = APIRouter()

# to get file path from url path parameters
@router.get("/url1/{filePath:path}")
async def file(filePath: str):
    return {"File path": filePath}


#getting user info
@router.post("/user/")
def user_details(user: schemas.User):
    return {'data': f'User is {user}'}


#path parmeter with numeric validation
@router.get('/user/validation/{userId}')
async def user_info(
    *, userId: int = Path(..., title="The ID of the user to get", ge=1, le=1000),
    q: str, grade: float = Query(..., gt=0, lt=10.5) 
                  ):
    return {'data': f'{userId} is user ID with details as {q} and grade as {grade}'}


# dropdown menu
@router.get('/modeloption/{models}')
async def drop_down(models: schemas.MachineLearningModel):
    message = await functions.model_info(models)
    return message


# using BaseModel
@router.post('/items/')
async def item(item: schemas.Items):
    return {'itemsInfo': f"itemName: {item.item_name} with quantity: {item.quantity} is to be bought {item.buy}"}


# query parameters with string validation
@router.post('/query/{queryId}')
def queries(
    queryId: int, queryType: str, 
    priorityHigh: Optional[bool] = False, comment: Optional[str] = Query(..., min_length=3, max_lenght=20),
    opinion: Optional[str] = Query(None, min_length=3, max_lenght=20), q: Optional[List[str]] = Query(None, title="Query string", description="Query string for the items to search in the database that have a good match", deprecated=True)
        ):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return {'data':f'query ID is {queryId} of type {queryType} with High priority as {priorityHigh} having comment as {comment} and your opinion {opinion} and additional q as {results}'}