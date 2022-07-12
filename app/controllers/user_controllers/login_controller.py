from http import HTTPStatus

from app.models.pessoa_model import Pessoa
from app.schemas import login_user_schema
from flask import request
from flask_expects_json import expects_json
from flask_jwt_extended import create_access_token
from werkzeug.exceptions import NotFound


@expects_json(login_user_schema)
def login_user():
    try:
        body = request.get_json()
        user: Pessoa = Pessoa.query.filter_by(cpf=body["cpf"]).first_or_404(
            description={"erro": "Usuário não encontrado."}
        )

        if not user.verify_password(body["password"]):
            return {"erro": "Email ou senha incorreto."}, HTTPStatus.FORBIDDEN

        token = create_access_token(identity={"idPessoa": user.idPessoa})

        return {"token": token}
    except NotFound as e:
        return e.description, HTTPStatus.NOT_FOUND
