# config.py
import os


class Config:
    SECRET_KEY = 'your_secret_key'
    SQLALCHEMY_DATABASE_URI = 'mysql://root:LicenceMonetiqueWeb@229@localhost/analyse_base'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
