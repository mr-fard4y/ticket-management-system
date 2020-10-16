# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------
#
# ---------------------------------------------------------------------
# Copyright (C) 2019-Present
# See LICENSE for details
# ---------------------------------------------------------------------

import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    VERSION = '0.0.1'
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    DEBUG = False
    TESTING = False
    ENV = 'production'


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