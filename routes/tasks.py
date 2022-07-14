from fastapi import APIRouter
from fastapi import HTTPException
from fastapi.encoders import jsonable_encoder
from uuid  import uuid4
from datetime import datetime

# Local imports
from schemas import Task
from config import tasks

task = APIRouter()

# Methods for Tasks
@task.get('/{id_user}')
def get_all_task(id_user: str):
    # Search for task in database
    task_dict = {}
    if tasks.__len__() > 0:
        for task in tasks:
            task_dict[task['id']] = task
        return task_dict
    # If not found, return 404
    raise HTTPException(status_code=404, detail=f'User: {id} not found')

@task.get('/{id_user}/{id_task}')
def get_task(id_user: str, id_task: str):
    # Search for task in database
    if True:
        return {'message': f'Task {id_task}'}
    # If not found, return 404
    raise HTTPException(status_code=404, detail=f'task: {id_task} for {id_user} not found')

@task.post('/{id_user}')
def create_task(id_user: str, task: Task):
    tasks.append(jsonable_encoder(task))
    task.id_user = id_user
    return task

@task.put('/{id_user}/{id_task}')
def update_task(id_user: str, id_task: str, task: Task):
    # Search for task in database
    if True:
        return {'message': f'Task {id}'}
    # If not found, return 404
    raise HTTPException(status_code=404, detail=f'task: {id} not found')

@task.delete('/{id_user}/{id_task}')
def delete_task(id_user: str, id_task: str):
    # Search for task in database
    if True:
        return {'message': f'Task {id}'}
    # If not found, return 404
    raise HTTPException(status_code=404, detail=f'task: {id} not found')
