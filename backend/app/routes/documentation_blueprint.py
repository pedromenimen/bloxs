from app.controllers.documentation_controllers import get_documentation, get_json
from flask import Blueprint

bp_doc = Blueprint("documentation", __name__, url_prefix="/api")

bp_doc.get("/rapidoc-json/")(get_json)
bp_doc.get("/docs/")(get_documentation)
