from fastapi import FastAPI
from http import HTTPStatus
from back.routers import users, complaints

app = FastAPI()

app.include_router(users.router)
app.include_router(complaints.router)

@app.get('/', status_code=HTTPStatus.OK)  
def read_root():  
    return {'message': 'Olá Mundo!'}