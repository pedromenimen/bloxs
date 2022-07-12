from flask import Flask
from flask_mysqldb import MySQL


def init_app(app:Flask):
    mysql = MySQL(app)
