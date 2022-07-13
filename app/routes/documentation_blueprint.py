from app.controllers.documentation_controllers import get_documentation, get_json
from flask import Blueprint

bp_doc = Blueprint("documentation", __name__,)

bp_doc.get("/api/rapidoc-json/")(get_json)
bp_doc.get("/")(get_documentation)
