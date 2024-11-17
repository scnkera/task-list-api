from flask import Blueprint, abort, make_response
# from ..models.task import tasks

tasks_bp = Blueprint("tasks_bp", __name__, url_prefix="/tasks")

# @tasks_bp.get("")
# def get_all_tasks():
#     results_list = []

#     for task in tasks:
#         results_list.append(task.to_dict())
        
#     return results_list


# @tasks_bp.get("/<task_id>")
# def get_one_task(task_id):
#     task = validate_task(task_id)
#     return task.to_dict(), 200

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