

from flask import Flask
from config import config


def create_app(app_stage='prod'):
    app = Flask(__name__)

    config_settings = config[app_stage]
    app.config.from_object(config_settings)

    register_blueprints(app)
    return app


def register_blueprints(app):
    pass
