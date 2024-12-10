from flask import abort, make_response
from ..db import db
from app.models.task import Task
from app.models.goal import Goal
from sqlalchemy import desc, asc

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

# def create_model(cls, model_data):
#     try:
#         new_model = cls.from_dict(model_data)
        
#     except KeyError as error:
#         response = {"details": "Invalid data"}
#         abort(make_response(response, 400))
    
#     db.session.add(new_model)
#     db.session.commit()

#     return new_model.to_dict(), 201

def get_models_filtered(cls, filter_params=None):
    query = db.select(cls)
    
    if filter_params:
        # Set default order_by attribute
        order_by = getattr(cls, filter_params.get("order_by", "title"))
        
        # Apply sorting based on the "sort" parameter
        if filter_params.get("sort") == "desc":
            query = query.order_by(desc(order_by))
        else:  # Default to ascending order
            query = query.order_by(asc(order_by))
    
    return query


# def validate_model_id(cls, model_id):
#     # checks for valid input
#     try:
#         model_id = int(model_id)
#     except:
#         response = {"msg": f"{cls.__name__} id {model_id} is invalid"}
#         abort(make_response(response, 400))

#     # returns task with the corresponding task_id
#     query = db.select(cls).where(cls.id == model_id)
#     model = db.session.scalar(query)

#     if not model:
#         response = {"msg": f"{cls.__name__} {model_id} not found."}
#         abort(make_response(response, 404))

#     return model

# route_utilities.py
