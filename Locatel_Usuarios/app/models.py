from flask_login import UserMixin
from . import db

class Usuario(db.Model):
    __tablename__ = 'usuario'
    cedula = db.Column(db.Integer, primary_key=True, autoincrement=False)
    nombre = db.Column(db.String(100))
    puntos = db.Column(db.Integer)
    ubicacion_id = db.Column(db.Integer, db.ForeignKey('ubicacion.id'))
    ubicacion = db.relationship("Ubicacion")

class Ubicacion(db.Model):
    __tablename__ = 'ubicacion'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100))
    valor_obtencion = db.Column(db.Float())
    valor_redencion = db.Column(db.Float())