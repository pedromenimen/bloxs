from dataclasses import dataclass
from datetime import datetime
from email.policy import default

from app.configs.database import db
from sqlalchemy.orm import relationship


@dataclass
class Transacao(db.Model):

    __tablename__ = "Transacao"

    idTransacao: int = db.Column(db.Integer, primary_key=True)
    idConta: int = db.Column(db.Integer, db.ForeignKey("Conta.idConta"))
    valor: float = db.Column(db.Float(2), nullable=False)
    dataTransacao: str = db.Column(db.DateTime, default=datetime.now)

    conta = relationship("Conta", back_populates="transacoes", uselist=False)
