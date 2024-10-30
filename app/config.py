# app/config.py

import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://user:password@127.0.0.1:3306/desafio_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
