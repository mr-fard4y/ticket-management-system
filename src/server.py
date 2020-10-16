

from flask import Flask
from config import config
from mongoengine.connection import connect as mongo_connect
from src.main.encoder import JSONEncoder


def create_app(app_stage='prod'):
    app = Flask(__name__)

    config_settings = config[app_stage]
    app.config.from_object(config_settings)

    app.json_encoder = JSONEncoder

    mongo_connect(
        host=app.config['MONGO_URI'],
        serverSelectionTimeoutMS=2000
    )

    register_blueprints(app)
    return app


def register_blueprints(app):
    from src.main.converter import RegexConverter
    app.url_map.converters['regex'] = RegexConverter

    from src.api import bp_api
    app.register_blueprint(bp_api, url_prefix='/api')

    from src.main import bp_main
    app.register_blueprint(bp_main)
