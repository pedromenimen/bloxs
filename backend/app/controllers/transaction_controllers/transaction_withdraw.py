from http import HTTPStatus

from app.configs.database import db
from app.models import Conta, Pessoa, Transacao
from app.schemas import transaction_schema
from flask import jsonify, request
from flask_expects_json import expects_json
from flask_jwt_extended import get_jwt_identity, jwt_required
from werkzeug.exceptions import NotFound


@jwt_required()
@expects_json(transaction_schema)
def transaction_withdraw():
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
        body = request.get_json()
        transaction: Transacao = Transacao(idConta=account.idConta, valor=body["valor"])
        if transaction.valor > account.saldo:
            return (
                jsonify({"erro": f"Saldo insuficiente. Saldo atual: {account.saldo}"}),
                HTTPStatus.UNPROCESSABLE_ENTITY,
            )
        account.withdraw(transaction.valor)
        db.session.add(transaction)
        db.session.commit()
        last_transaction = Transacao.query.filter_by(
            idTransacao=transaction.idTransacao
        ).first()
        account.dataCriacao = last_transaction.dataTransacao
        return jsonify(account), HTTPStatus.OK
    except NotFound as e:
        return e.description, HTTPStatus.NOT_FOUND
