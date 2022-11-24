from fastapi import FastAPI

from fastapi import APIRouter

from myapp.todo.src.infrastructure.rest import controllers

api_router = APIRouter()
api_router.include_router(controllers.router)

app = FastAPI()

app.include_router(api_router)



@app.get("/")
async def root():
    return {"message": "Hello World"}



