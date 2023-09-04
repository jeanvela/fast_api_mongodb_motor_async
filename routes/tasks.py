from fastapi import APIRouter, HTTPException
from db import get_all_tasks, get_one_task_id, create_task, update_task, delete_task, get_one_task
from models.task import updateTask, Task
from bson import ObjectId

task = APIRouter()

@task.get('/api/tasks')
async def get_tasks():
    all_tasks = await get_all_tasks()
    return all_tasks

@task.post('/api/tasks/create')
async def save_task(task:Task):
    # new_task = ObjectId(task.id)
    # task
    # print(new_task)
    task_found = await get_one_task(task.title)
    if task_found:
        raise HTTPException(409, 'Task already exists')
    response = await create_task(task.dict())
    if response:
        print(response)
        return response
    raise HTTPException(404, 'Something went wrong')

@task.get('/api/tasks/{id}', response_model=Task)
async def get_task(id: str):
    if not ObjectId(id):
        raise HTTPException(404, 'pruaba')
    task = await get_one_task_id(id)
    if task:
        return task
    raise HTTPException(404, f'Task with id {id} not found')

@task.put('/api/tasks/put/{id}', response_model=updateTask)
async def put_task(id: str, task:updateTask):
    response =await update_task(id, task)
    if response:
        return response
    raise HTTPException(404, f'Task with id {id} not found')

@task.delete('/api/tasks/delete/{id}')
async def remove_task(id: str):
    response = await delete_task(id)
    if response:
        return 'Successfully deleted task'
    raise HTTPException(404, f'Task with id {id} not found')

@task.post('/api/taskCreate')
async def post(task: updateTask):
    return 'hola'