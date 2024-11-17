from flask import Blueprint, abort, make_response, request
from ..db import db
from app.models.task import Task

tasks_bp = Blueprint("tasks_bp", __name__, url_prefix="/tasks")

@tasks_bp.post("")
def create_cat():
    request_body = request.get_json()
    title = request_body["title"]
    description = request_body["description"]
    completed_at = request_body["completed_at"]

    new_task = Task(title=title, description=description, completed_at=completed_at)
    db.session.add(new_task)
    db.session.commit()

    response = new_task.to_dict()
    return response, 201

@tasks_bp.get("")
def get_all_cats():
    query = db.select(Task).order_by(Task.id)
    tasks = db.session.scalars(query)

    tasks_response = [task.to_dict() for task in tasks]
    return tasks_response

def validate_task(task_id):

    # checks for valid input
    try: 
        task_id = int(task_id)
    except: 
        abort(make_response({"message": f"Task id {task_id} not found"}, 400))

    # returns task with the corresponding task_id
    for task in tasks:
        if task.id == task_id:
            return task
        
    abort(make_response({"message": f"Task id {task_id} not found"}, 404))