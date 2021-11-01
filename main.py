from fastapi import FastAPI
import uvicorn
from subresources.sql_app import sqlModel, database
from subresources.routers import sqLRouterEmployee, sqLRouterEmployer, basicRouter

app = FastAPI()

sqlModel.Base.metadata.create_all(database.engine)

app.include_router(sqLRouterEmployee.router)
app.include_router(sqLRouterEmployer.router)
app.include_router(basicRouter.router)



# to get file path from url path parameters in basic router

#sql apps in router part employee and employer seperated



# if __name__ == "__main__":
#     uvicorn.run(app, host='localhost', port=8000, debug=True)