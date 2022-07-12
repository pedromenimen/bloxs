from http import HTTPStatus

from app.models import Conta, Pessoa, Transacao
from flask import jsonify, request
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
            page = request.args.get("page", 1, type=int)
            transaction_list = Transacao.query.filter_by(idConta=account.idConta)
            pagination = transaction_list.paginate(
                page=page, per_page=10, error_out=False
            )
            return jsonify(pagination.items), HTTPStatus.OK
    except NotFound as e:
        return e.description, HTTPStatus.NOT_FOUND
