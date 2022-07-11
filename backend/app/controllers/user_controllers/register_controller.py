from http import HTTPStatus

from app.configs.database import db
from app.models.pessoa_model import Pessoa
from app.schemas import register_user_schema
from flask import jsonify, request
from flask_expects_json import expects_json
from sqlalchemy.exc import IntegrityError
from werkzeug.exceptions import BadRequest


@expects_json(register_user_schema)
def create_user():
    try:
        body = request.get_json()
        password_to_hash = body.pop("password")
        cpf:str = body.pop("cpf")
        new_user = Pessoa(**body, cpf=cpf.replace("-", "").replace(".", ""))
        new_user.password = password_to_hash
        db.session.add(new_user)
        db.session.commit()
        return jsonify(new_user), 201
    except BadRequest as e:
        return e.description, HTTPStatus.BAD_REQUEST
    except IntegrityError as e:
        field = str(e.orig).split("Key")[1].split("=")[0][2:-1]
        return (
            jsonify({"erro": f"{field[0].upper()+field[1:]} já cadastrado."}),
            HTTPStatus.CONFLICT,
        )
    except TypeError as e:
        invalid_field = e.args[0].split(" is an invalid")[0].strip("'")
        return jsonify({"erro": f"Campo inválido: {invalid_field}."}), 400
