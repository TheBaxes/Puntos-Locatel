import datetime
from flask_login import UserMixin
from . import db

class Usuario(UserMixin, db.Model):
    __tablename__ = 'usuario'
    cedula = db.Column(db.Integer, primary_key=True, autoincrement=False)
    nombre = db.Column(db.String(100))
    password = db.Column(db.String(100))
    tarjeta_id = db.Column(db.Integer, db.ForeignKey('tarjeta.id'))
    tarjeta = db.relationship("Tarjeta", backref=db.backref("usuario", uselist=False))
    def get_id(self):
        return self.cedula

class Tarjeta(db.Model):
    __tablename__ = 'tarjeta'
    id = db.Column(db.Integer, primary_key=True, autoincrement=False)
    puntos = db.Column(db.Integer)
    ubicacion_id = db.Column(db.Integer, db.ForeignKey('ubicacion.id'))
    ubicacion = db.relationship("Ubicacion")
    facturas = db.relationship("Factura")


class Ubicacion(db.Model):
    __tablename__ = 'ubicacion'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100))
    valor_obtencion = db.Column(db.Float())
    valor_redencion = db.Column(db.Float())
    codigo = db.Column(db.String(3))
    ratio = db.Column(db.Float())
    productos = db.relationship("Producto_Ubicacion")

class Producto(db.Model):
    __tablename__ = 'producto'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100))
    imagen = db.Column(db.String(100))


class Producto_Ubicacion(db.Model):
    __tablename__ = 'producto_ubicacion'
    id = db.Column(db.Integer, primary_key=True)
    ubicacion_id = db.Column(db.Integer, db.ForeignKey('ubicacion.id'))
    producto_id = db.Column(db.Integer, db.ForeignKey('producto.id'))
    precio = db.Column(db.Float)
    producto = db.relationship("Producto")

class Factura(db.Model):
    __tablename__ = 'factura'
    id = db.Column(db.Integer, primary_key=True)
    productos = db.Column(db.String(1000))
    precios = db.Column(db.String(1000))
    total = db.Column(db.Float)
    fecha = db.Column(db.DateTime(timezone=True), default=datetime.datetime.utcnow)
    puntos = db.Column(db.Integer)
    tarjeta_id = db.Column(db.Integer, db.ForeignKey('tarjeta.id'))
    ubicacion_id = db.Column(db.Integer, db.ForeignKey('ubicacion.id'))
    ubicacion = db.relationship("Ubicacion")
