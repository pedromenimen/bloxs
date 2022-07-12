from flask import Flask
from flask_cors import CORS


from app import routes
from app.configs import Config, database, jwt_authentication, migration, mysql

def create_app():
    app = Flask(__name__)

    app.config.from_object(Config)
    CORS(
        app,
        origins=["http://localhost:5000"],
        methods=["GET", "POST", "PATCH", "DELETE"],
    )
    mysql.init_app(app)
    routes.init_app(app)
    database.init_app(app)
    migration.init_app(app)
    jwt_authentication.init_app(app)
    return app
