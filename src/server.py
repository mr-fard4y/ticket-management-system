

from flask import Flask
from config import config


def create_app(app_stage='prod'):
    app = Flask(__name__)

    config_settings = config[app_stage]
    app.config.from_object(config_settings)

    register_blueprints(app)
    return app


def register_blueprints(app):
    from src.api import bp_api
    app.register_blueprint(bp_api, url_prefix='/api')

    from src.main import bp_main
    app.register_blueprint(bp_main)
