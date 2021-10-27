from typing import Optional
from fastapi import FastAPI
import uvicorn
from subresources import schemas
from subresources import functions
app = FastAPI()

# to get file path from url
@app.get("/url1/{filePath:path}")
async def file(filePath: str):
    return {"File path": filePath}


#getting user info
@app.post("/user/")
def user_details(user: schemas.User):
    return {'data':f'User is {user}'}


# dropdown menu
@app.get('/modeloption/{models}')
async def option(models: schemas.MachineLearningModel):
    message = functions.model_info(models)
    return message

# using BaseModel
@app.post('/items/')
async def item(item: schemas.Items):
    return {'itemsInfo': f"itemName: {item.item_name} with quantity: {item.quantity} is to be bought {item.buy}"}


# query parameters
@app.post('/query/{queryId}')
def queries(queryId: int, queryType: str, priorityHigh: Optional[bool] = False):
    return {'data':f'query ID is {queryId} of type {queryType} with High priority as {priorityHigh}'}


# if __name__ == "__main__":
#     uvicorn.run(app, host='localhost', port=8000, debug=True)