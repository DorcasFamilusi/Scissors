import os

# SQLALCHEMY_DATABASE_URI = 'sqlite:///db.sqlite3'
# SQLALCHEMY_TRACK_MODIFICATIONS = False
# SECRET_KEY = os.environ.get('SECRET_KEY')
# ADMIN_USERNAME = os.environ.get('ADMIN_USERNAME')
# ADMIN_PASSWORD = os.environ.get('ADMIN_PASSWORD')


default_uri = "postgres://{}:{}@{}/{}".format('postgres', 'password', 'localhost:5432', 'scissors_app_db')

uri = os.getenv('DATABASE_URL', default_uri) # or other relevant config var
if uri.startswith('postgres://'):
    uri = uri.replace('postgres://', 'postgresql://', 1)

class Config:
    SECRET_KEY = '4128c5e3a66aba8278a0f4523f123d9c'

class DevConfig(Config):
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///db.sqlite3' #os.environ.get('DATABASE_URL')

class TestConfig(Config):
    TESTING = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_DATABASE_URI = 'sqlite://'

class ProdConfig(Config):
    DEBUG = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = uri


config_dict = {
    'dev': DevConfig,
    'test': TestConfig,
    'prod': ProdConfig
}