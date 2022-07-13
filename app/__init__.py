from flask import Flask
from flask_cors import CORS


from app import routes
from app.configs import Config, database, jwt_authentication, migration

def create_app():
    app = Flask(__name__)

    app.config.from_object(Config)
    CORS(
        app,
        origins=["http://localhost:5000","http://127.0.0.1:5000"],
        methods=["GET", "POST", "PATCH", "DELETE"],
    )
    routes.init_app(app)
    database.init_app(app)
    migration.init_app(app)
    jwt_authentication.init_app(app)
    return app
