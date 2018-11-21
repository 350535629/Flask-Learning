# -*- coding: utf-8 -*-

import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'
    #SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    FLASK_MAIL_SUBJECT_PREFIX = '[FLASK]'
    FLASK_MAIL_SENDER = 'Baymax <350535629@qq.com>'
    FLASK_ADMIN = os.environ.get('FLASK_ADMIN')

    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    DEBUG = False
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    #SQLALCHEMY_DATABASE_URI

class TestingConfig(Config):
    TESTING = True
    #SQL

#class ProductionConfig(Config):
    #SQL

config = {
    'development': DevelopmentConfig,
    'tetsing': TestingConfig,
#    'production': ProductionConfig,
    'default': DevelopmentConfig
}
