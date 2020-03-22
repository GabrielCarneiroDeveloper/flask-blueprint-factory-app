import os


class Config(object):
    DEBUG = False
    TESTING = False
    DATABASE_URI = 'sqlite:///:memory:'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = f'sqlite:///{os.path.abspath(".")}/data.db'
    API_VERSION = 'v1'


class Production(Config):
    ENV = 'Production'
    HOST = '0.0.0.0'
    DATABASE_URI = 'mysql://user@localhost/foo'
    PORT = '5010'
    SECRET_KEY = 'secret_key_prod'


class Development(Config):
    ENV = 'Development'
    HOST = '0.0.0.0'
    DEBUG = True
    PORT = '5000'
    SECRET_KEY = 'secret_key_dev'


class Test(Config):
    ENV = 'Test'
    HOST = '0.0.0.0'
    TESTING = True
    PORT = '3214'
    SECRET_KEY = 'secret_key_test'
