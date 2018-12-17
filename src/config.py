# /src/config.py

import os

class Development(object):
    """
    Development environment configuration
    """
    DEBUG = True
    TESTING = False
    JWT_SECRET_KEY = 'hhgaghhgsdhdhdd'
    SQLALCHEMY_DATABASE_URI = 'postgres://jhenbvzzxcjukg:f2f44fb6e0a10677c848586917f80cccae04d488bd03f809ba98398edad3030d@ec2-54-217-237-93.eu-west-1.compute.amazonaws.com:5432/d87uli0648co1c'

class Production(object):
    """
    Production environment configurations
    """
    DEBUG = False
    TESTING = False #estava a false
    SQLALCHEMY_DATABASE_URI = 'postgres://jhenbvzzxcjukg:f2f44fb6e0a10677c848586917f80cccae04d488bd03f809ba98398edad3030d@ec2-54-217-237-93.eu-west-1.compute.amazonaws.com:5432/d87uli0648co1c'
    JWT_SECRET_KEY = 'hhgaghhgsdhdhdd'

app_config = {
    'development': Development,
    'production': Production,
}
