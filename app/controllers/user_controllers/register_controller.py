from http import HTTPStatus

from app.configs.database import db
from app.models.pessoa_model import Pessoa
from app.schemas import register_user_schema
from flask import jsonify, request
from flask_expects_json import expects_json
from werkzeug.exceptions import BadRequest, NotFound


@expects_json(register_user_schema)
def create_user():
    try:
        body = request.get_json()
        password_to_hash = body.pop("password")
        cpf: str = body.pop("cpf")
        dataNascimento = body.pop("dataNascimento")
        dataNascimentoFormatada = Pessoa.format_datetime(dataNascimento)
        user = Pessoa.query.filter_by(cpf=cpf).first()
        if user:
            return jsonify({"erro": "Esse cpf já está em uso."})
        new_user = Pessoa(
            **body,
            cpf=cpf.replace("-", "").replace(".", ""),
            dataNascimento=dataNascimentoFormatada,
        )
        new_user.password = password_to_hash
        db.session.add(new_user)
        db.session.commit()
        return jsonify(new_user), 201
    except BadRequest as e:
        return e.description, HTTPStatus.BAD_REQUEST
    except NotFound as e:
        return e.description, HTTPStatus.NOT_FOUND
