import sqlalchemy
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db: sqlalchemy = SQLAlchemy()


def init_app(app: Flask):

    db.init_app(app)
    app.db = db

    from app.models import Conta, Pessoa, Transacao
