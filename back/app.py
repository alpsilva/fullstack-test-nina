from back.routers import users, complaints
from fastapi import FastAPI
from http import HTTPStatus

app = FastAPI()

app.include_router(users.router)
app.include_router(complaints)

@app.get('/', status_code=HTTPStatus.OK)  
def read_root():  
    return {'message': 'Olá Mundo!'}