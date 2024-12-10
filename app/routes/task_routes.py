from flask import Blueprint, abort, make_response, request, Response
from ..db import db
from app.models.task import Task
from .route_utilities import validate_model, create_model, get_models_with_filters
# from app.routes.route_utilities import validate_model_id

tasks_bp = Blueprint("tasks_bp", __name__, url_prefix="/tasks")

@tasks_bp.post("")
def create_task():
    request_body = request.get_json()

    return create_model(Task, request_body)

@tasks_bp.get("")
def get_all_tasks():

    return get_models_with_filters(Task, request.args)

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

@tasks_bp.path("/<task_id>/mark_complete")
def mark_task_complete(task_id):
    pass

@tasks_bp.path("/<task_id>/mark_incomplete")
def mark_task_incomplete(task_id):
    pass