from fastapi import FastAPI

app = FastAPI()  

@app.get('/complaints')  
def read_root():  
    return {'message': 'Olá Mundo!'}