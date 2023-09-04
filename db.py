from motor.motor_asyncio import AsyncIOMotorClient
from models.task import Task
from bson import ObjectId

client = AsyncIOMotorClient('mongodb://127.0.0.1')

database = client.taskDataBase

Tasks = database.tasks

async def get_one_task_id(id):
    task = await Tasks.find_one({'_id': ObjectId(id)})  #* El id lo convertimos en un ObjectoId
    return task

async def get_one_task(title: str):
    one_task = await Tasks.find_one({'title': title})
    return one_task

async def get_all_tasks():
    tasks = []
    cursor = Tasks.find({})
    async for document in cursor:
        tasks.append(Task(**document))
    return tasks

async def create_task(task):
    new_id = str(ObjectId())
    task['_id'] = new_id
    new_task = await Tasks.insert_one(task)
    found_task = await Tasks.find_one({'_id': new_task.inserted_id})
    return found_task

async def update_task(id: str, data):
    task = {
        k:v for k, v in data.dict().items() if v is not None
        # Todo: Convertimos data en un diccionario, si el valor que esta reciviendo es none
        #* cada que recorra cada clave valor y vemos que none no lo va añadir
        #* solo si tiene algo adentro es el valor que va aguardar
    }
    await Tasks.update_one({'_id': ObjectId(id)}, {'$set': task})
    document = await Tasks.find_one({'_id': ObjectId(id)})
    return document

async def delete_task(id: str):
    await Tasks.delete_one({'_id': ObjectId(id)})
    return True