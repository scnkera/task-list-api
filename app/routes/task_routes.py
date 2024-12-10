from flask import Blueprint, abort, make_response, request, Response
from ..db import db
from app.models.task import Task
# from app.routes.route_utilities import validate_model_id, create_model

tasks_bp = Blueprint("tasks_bp", __name__, url_prefix="/tasks")

@tasks_bp.post("")
def create_task():

    request_body = request.get_json()

    if "title" not in request_body or "description" not in request_body:
        return {"details": "Invalid data"}, 400

    new_task = Task.from_dict(request_body)

    db.session.add(new_task)
    db.session.commit()


    # response = new_task.to_dict()
    response = {"task": new_task.to_dict()}
    return response, 201

@tasks_bp.get("")
def get_all_tasks():
    query = db.select(Task).order_by(Task.id)
    tasks = db.session.scalars(query)

    tasks_response = [task.to_dict() for task in tasks]
    # tasks_response = [{"task": task.to_dict()} for task in tasks]
    return tasks_response

@tasks_bp.get("/<task_id>")
def get_single_task(task_id):
    task = validate_model(Task, task_id)

    return {"task": task.to_dict()}

@tasks_bp.put("/<task_id>")
def update_task(task_id):
    task = validate_model(Task, task_id)

    request_body = request.get_json()
    task.title = request_body["title"]
    task.description = request_body["description"]

    db.session.commit()

    return {"task": task.to_dict()}

@tasks_bp.delete("/<task_id>")
def delete_task(task_id):
    task = validate_model(Task, task_id)

    db.session.delete(task)
    db.session.commit()

    response = {"details": f"Task {task_id} \"{task.title}\" successfully deleted"}

    return response

def validate_model(cls, model_id):

    # checks for valid input
    try: 
        model_id = int(model_id)
    except: 
        abort(make_response({"message": f"Task id {model_id} not found"}, 400))

    # returns task with the corresponding task_id
    query = db.select(cls).where(cls.id == model_id)
    model = db.session.scalar(query)

    if not model:
        abort(make_response({"message": f"Task id {model_id} not found"}, 404))

    return model


def create_model(cls, model_data):
    try:
        new_model = cls.from_dict(model_data)
        
    except KeyError as error:
        response = {"details": "Invalid data"}
        abort(make_response(response, 400))
    
    db.session.add(new_model)
    db.session.commit()

    return new_model.to_dict(), 201