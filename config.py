
import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    VERSION = '0.0.1'
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    DEBUG = False
    TESTING = False
    ENV = 'production'
    MONGO_URI = os.environ.get('APP_DB') or 'mongodb://127.0.0.1:27017/flights_app'


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    TESTING = True


class ProductionConfig(Config):
    pass


config = {
    'prod': ProductionConfig,
    'test': TestingConfig,
    'dev': DevelopmentConfig
}