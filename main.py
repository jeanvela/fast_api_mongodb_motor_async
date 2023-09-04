from fastapi import FastAPI
from routes.tasks import task

app = FastAPI()


@app.get('/')
def welcome():
    return {'message': 'welcome to my FastApi'}

app.include_router(task)