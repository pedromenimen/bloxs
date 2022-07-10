from http import HTTPStatus

from app.models import Conta, Pessoa
from flask import jsonify
from flask_jwt_extended import get_jwt_identity, jwt_required
from werkzeug.exceptions import NotFound


@jwt_required()
def check_transactions():
    try:
        user_id = get_jwt_identity()["idPessoa"]
        user: Pessoa = Pessoa.query.filter_by(idPessoa=user_id).first_or_404(
            description={"erro": "Usuário não encontrado."}
        )
        if not user.Conta:
            return jsonify({"erro": "Você não tem uma conta."}), HTTPStatus.NOT_FOUND
        account: Conta = user.Conta
        if not account.flagAtivo:
            return jsonify({"erro": "Esta conta está bloqueada."}), HTTPStatus.FORBIDDEN
        if len(account.transacoes) == 0:
            return (
                jsonify({"erro": "Você ainda não realizou nenhuma transação."}),
                HTTPStatus.UNPROCESSABLE_ENTITY,
            )
        else:
            return jsonify(account.transacoes), HTTPStatus.OK
    except NotFound as e:
        return e.description, HTTPStatus.NOT_FOUND
