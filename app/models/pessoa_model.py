from dataclasses import dataclass
from datetime import datetime

import sqlalchemy as sql
from app.configs.database import db
from werkzeug.security import check_password_hash, generate_password_hash


@dataclass
class Pessoa(db.Model):

    __tablename__ = "Pessoa"

    idPessoa: int = sql.Column(sql.Integer, primary_key=True)
    nome: str = sql.Column(sql.String(150), nullable=False)
    cpf: str = sql.Column(sql.String(11), nullable=False, unique=True)
    dataNascimento: str = sql.Column(sql.Date, nullable=False)
    password_hash = db.Column(db.String(150), nullable=True)

    @property
    def password(self):
        raise AttributeError("A senha não pode ser acessada")

    @password.setter
    def password(self, password_to_hash):
        self.password_hash = generate_password_hash(password_to_hash)

    def verify_password(self, password_to_compare):
        return check_password_hash(self.password_hash, password_to_compare)

    def format_datetime(value, format="%Y/%m/%d"):
        return datetime.strptime(value, "%d/%m/%Y").strftime(format)
