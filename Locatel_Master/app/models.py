from flask_login import UserMixin
from . import db

class Ubicacion(db.Model):
    __tablename__ = 'ubicacion'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100))
    valor_obtencion = db.Column(db.Float())
    valor_redencion = db.Column(db.Float())

class Master(UserMixin, db.Model):
    __tablename__ = 'master'
    cedula = db.Column(db.Integer, primary_key=True, autoincrement=False)
    password = db.Column(db.String(100))
    ubicacion_id = db.Column(db.Integer, db.ForeignKey('ubicacion.id'))
    ubicacion = db.relationship('Ubicacion')

    def get_id(self):
        return self.cedula
