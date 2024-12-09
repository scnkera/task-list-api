from flask import abort, make_response
from ..db import db
from app.models.task import Task
from app.models.goal import Goal
from sqlalchemy import desc, asc

def validate_model_id(cls, model_id):
    # checks for valid input
    try:
        model_id = int(model_id)
    except:
        response = {"msg": f"{cls.__name__} id {model_id} is invalid"}
        abort(make_response(response, 400))

    # returns task with the corresponding task_id
    query = db.select(cls).where(cls.id == model_id)
    model = db.session.scalar(query)

    if not model:
        response = {"msg": f"{cls.__name__} {model_id} not found."}
        abort(make_response(response, 404))

    return model

def create_model(cls, model_data):
    valid_model_data = validate_new_model_data(cls, model_data)

    new_model = cls.from_dict(valid_model_data)
    db.session.add(new_model)
    db.session.commit()

    response = {cls.__name__.lower(): new_model.to_dict()}
    return response, 201

# def validate_task(task_id):

#     # checks for valid input
#     try: 
#         task_id = int(task_id)
#     except: 
#         abort(make_response({"message": f"Task id {task_id} not found"}, 400))

#     # returns task with the corresponding task_id
#     query = db.select(Task).where(Task.id == task_id)
#     task = db.session.scalar(query)

#     if not task:
#         abort(make_response({"message": f"Task id {task_id} not found"}, 404))

#     return task