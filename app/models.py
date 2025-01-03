from app import db
from datetime import datetime, timezone

class Contato(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data_envio = db.Column(db.DateTime, default=datetime.now(timezone.utc))
    nome = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    assunto = db.Column(db.String, nullable=False)
    mensagem = db.Column(db.String, nullable=False)
    respondido = db.Column(db.Integer, default=0)

