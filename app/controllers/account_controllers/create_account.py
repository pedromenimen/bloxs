from http import HTTPStatus

from app.configs.database import db
from app.models import Conta, Pessoa
from app.schemas.register_account_schema import register_account_schema
from flask import jsonify, request
from flask_expects_json import expects_json
from flask_jwt_extended import get_jwt_identity, jwt_required
from werkzeug.exceptions import NotFound


@jwt_required()
@expects_json(register_account_schema)
def create_account():
    try:
        body = request.get_json()
        user_id = get_jwt_identity()["idPessoa"]
        user: Pessoa = Pessoa.query.filter_by(idPessoa=user_id).first_or_404(
            description={"erro": "Usuário não encontrado."}
        )
        if user.Conta:
            return jsonify({"erro": "Você já tem uma conta."}), HTTPStatus.CONFLICT
        new_account = Conta(**body, saldo=0, flagAtivo=True, pessoa=user)
        db.session.add(new_account)
        db.session.commit()
        return jsonify(new_account), 201
    except NotFound as e:
        return e.description, HTTPStatus.NOT_FOUND
