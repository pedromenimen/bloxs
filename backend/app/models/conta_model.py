from dataclasses import dataclass
from datetime import datetime

from app.configs.database import db
from flask import jsonify
from sqlalchemy.orm import backref, relationship


@dataclass
class Conta(db.Model):

    __tablename__ = "Conta"

    idConta: int = db.Column(db.Integer, primary_key=True)
    idPessoa: int = db.Column(
        db.Integer, db.ForeignKey("Pessoa.idPessoa"), unique=True, nullable=False
    )
    saldo: float = db.Column(db.Float)
    limiteSaqueDiario: float = db.Column(db.Float)
    flagAtivo: bool = db.Column(db.Boolean)
    tipoConta: int = db.Column(db.Integer)
    dataCriacao: str = db.Column(db.DateTime, default=datetime.now)

    def deposit(self, value):
        self.saldo = round(self.saldo + value, 2)

    def withdraw(self, value):
        self.saldo = round(self.saldo - value, 2)

    pessoa = relationship("Pessoa", backref=backref("Conta", uselist=False))

    transacoes = relationship("Transacao", back_populates="conta")
