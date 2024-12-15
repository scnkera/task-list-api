from flask import Blueprint, abort, make_response, request, Response
from ..db import db
from ..models.goal import Goal
import datetime
import requests
import os
from sqlalchemy import desc, asc

goals_bp = Blueprint("goals_bp", __name__, url_prefix="/goals")

@goals_bp.post("")
def create_goal():
    request_body = request.get_json()

    try:
        title = request_body["title"]
    except KeyError:
        response = {"details": "Invalid data"}
        abort(make_response(response, 400))

    new_goal = Goal(title=title)

    db.session.add(new_goal)
    db.session.commit()

    response = {"goal": new_goal.to_dict()}
    return response, 201

@goals_bp.get("")
def get_all_goals():
    query = db.select(Goal).order_by(Goal.id)
    goals = db.session.scalars(query)

    response=[goal.to_dict() for goal in goals]

    return response, 200

@goals_bp.get("/<goal_id>")
def get_single_goal(goal_id):
    goal = validate_goal_id(goal_id)

    return {"goal": goal.to_dict()}, 200

@goals_bp.put("/<goal_id>")
def update_goal(goal_id):
    goal=validate_goal_id(goal_id)
    request_body = request.get_json()

    goal.title = request_body["title"]
    db.session.commit()

    response = {"title": goal.title}

    return response, 200

@goals_bp.delete("/<goal_id>")
def delete_goal(goal_id):
    goal = validate_goal_id(goal_id)
    
    db.session.delete(goal)
    db.session.commit()

    response = {"details": f"Goal {goal.id} \"{goal.title}\" successfully deleted"}
    return response, 200

def validate_goal_id(goal_id):
    try:
        goal_id = int(goal_id)
    except:
        response = {"msg": f"Goal_id {goal_id} is invalid"}
        abort(make_response(response, 400))

    query = db.select(Goal).where(Goal.id == goal_id)
    found_goal = db.session.scalar(query)

    if not found_goal:
        response = {"msg": f"Goal {goal_id} not found."}
        abort(make_response(response, 404))

    return found_goal