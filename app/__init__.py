from flask import Flask
from .routes.task_routes import tasks_bp

def create_app():
    # __name__ stores the name of the module we're in
    app = Flask(__name__)
    app.register_blueprint(tasks_bp)

    return app