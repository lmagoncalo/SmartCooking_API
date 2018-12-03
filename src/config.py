# /src/config.py

import os

class Development(object):
    """
    Development environment configuration
    """
    DEBUG = True
    TESTING = False
    JWT_SECRET_KEY = 'hhgaghhgsdhdhdd'
    SQLALCHEMY_DATABASE_URI = 'postgres://postgres:123456789@127.0.0.1:5432/smartcooking'

class Production(object):
    """
    Production environment configurations
    """
    DEBUG = False
    TESTING = False #estava a false
    SQLALCHEMY_DATABASE_URI = 'postgres://postgres:123456789@127.0.0.1:5432/smartcooking'
    JWT_SECRET_KEY = 'hhgaghhgsdhdhdd'

app_config = {
    'development': Development,
    'production': Production,
}