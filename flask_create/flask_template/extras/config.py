#By default configs are saved in .env file and loaded into env when app is running
#This provides a good security by not letting in important credentials into the code.

from dotenv import load_dotenv
from os import environ,path

#set sensitive values in .env file and load them to environment
base = path.abspath(path.dirname(__file__))
load_dotenv(path.join(base,'.env'))

#set all the config values here

class Config:
    FLASK_DEBUG = True
    FLASK_ENV = "development"
    DEBUG = True
    ENV = "development"
    SECRET_KEY = environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = environ.get('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
