from fastapi import FastAPI
from app.routes.employee_routes import router as employee_router

application = FastAPI()


@application.get("/")
def root():
    return {"Message": "Employee Management Backend is running!"}


application.include_router(employee_router)