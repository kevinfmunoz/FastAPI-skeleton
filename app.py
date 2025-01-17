from starlette.requests import Request
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from routes.users import user
from routes.tasks import task

app = FastAPI()

# Routes
app.include_router(user, prefix='/users')
app.include_router(task, prefix='/tasks')

# General Methods
@app.get('/')
@app.get('/home')
def root():
    # Validate if the users and passwords are correct
    return {'message': 'Hello World'}

@app.get('/test')
def test():
    resp = {'nombre':'Daniel', 'apellido': 'Cazabat', 'edad': 53}
    return resp