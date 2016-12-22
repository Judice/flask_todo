from flask import Flask
from flask_mongoengine import MongoEngine

db = MongoEngine()

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object('config')
    db.init_app(app)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
