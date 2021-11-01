from typing import Optional, List
from sqlalchemy.sql.expression import false
from fastapi import FastAPI, Query, Path, Depends, status, Response, HTTPException
import uvicorn
from subresources import schemas, functions
from subresources.sql_app import sqlModel, database
from subresources.routers import sql_router_employee, sql_router_employer, basic_router

app = FastAPI()

sqlModel.Base.metadata.create_all(database.engine)

app.include_router(sql_router_employee.router)
app.include_router(sql_router_employer.router)
app.include_router(basic_router.router)



# to get file path from url path parameters in basic router

#sql apps in router part employee and employer seperated



# if __name__ == "__main__":
#     uvicorn.run(app, host='localhost', port=8000, debug=True)