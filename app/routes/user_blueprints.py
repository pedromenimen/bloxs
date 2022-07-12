from app.controllers.user_controllers import create_user, login_user
from app.error_handling.error_handling import bad_request
from flask import Blueprint
from werkzeug.exceptions import BadRequest

bp_users = Blueprint("user", __name__, url_prefix="/api/user")


bp_users.app_errorhandler(BadRequest)(bad_request)
bp_users.post("/register/")(create_user)
bp_users.post("/login/")(login_user)
