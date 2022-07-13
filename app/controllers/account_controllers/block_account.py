from http import HTTPStatus

from app.configs.database import db
from app.models import Conta, Pessoa
from flask import jsonify
from flask_jwt_extended import get_jwt_identity, jwt_required
from werkzeug.exceptions import NotFound


@jwt_required()
def block_account():
    try:
        user_id = get_jwt_identity()["idPessoa"]
        user: Pessoa = Pessoa.query.filter_by(idPessoa=user_id).first_or_404(
            description={"erro": "Usuário não encontrado."}
        )
        if not user.Conta:
            return jsonify({"erro": "Você não tem uma conta."}), HTTPStatus.NOT_FOUND
        account: Conta = user.Conta
        if not account.flagAtivo:
            return (
                jsonify({"erro": "Esta conta já está bloqueada."}),
                HTTPStatus.FORBIDDEN,
            )
        if account.saldo > 0:
            return (
                jsonify(
                    {
                        "erro": "Você deve sacar todo o seu saldo antes de bloquear a conta."
                    }
                ),
                HTTPStatus.FORBIDDEN,
            )
        account.flagAtivo = False
        db.session.commit()
        return jsonify(None), HTTPStatus.NO_CONTENT
    except NotFound as e:
        return e.description, HTTPStatus.NOT_FOUND
