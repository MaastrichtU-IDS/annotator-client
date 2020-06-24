"""Default configuration

Use env var to override
"""
import os
import urllib.parse

ENV = os.getenv("FLASK_ENV")
DEBUG = ENV == "development"
SECRET_KEY = os.getenv("SECRET_KEY")

SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URI")
SQLALCHEMY_TRACK_MODIFICATIONS = False

JWT_BLACKLIST_ENABLED = True
JWT_BLACKLIST_TOKEN_CHECKS = ["access", "refresh"]

username = urllib.parse.quote_plus('admin')
password = urllib.parse.quote_plus('password')
mongodb_url = 'mongodb+srv://%s:%s@cluster0-ei2gj.mongodb.net/annotations?retryWrites=true&w=majority' % (username, password)
MONGODB_SETTINGS = {'host': mongodb_url}
