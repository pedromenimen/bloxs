from http import HTTPStatus

from app.models import Conta, Pessoa, Transacao
from flask import jsonify, request
from flask_jwt_extended import get_jwt_identity, jwt_required
from werkzeug.exceptions import NotFound


@jwt_required()
def transaction_check_balance():
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
        return jsonify(account), HTTPStatus.OK
    except NotFound as e:
        return e.description, HTTPStatus.NOT_FOUND
