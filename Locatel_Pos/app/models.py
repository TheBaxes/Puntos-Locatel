from . import db


class Ubicacion(db.Model):
    __tablename__ = 'ubicacion'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100))
    valor_obtencion = db.Column(db.Float())
    valor_redencion = db.Column(db.Float())
    productos = db.relationship("Producto_Ubicacion")


class Usuario(db.Model):
    __tablename__ = 'usuario'
    cedula = db.Column(db.Integer, primary_key=True, autoincrement=False)
    nombre = db.Column(db.String(100))
    password = db.Column(db.String(100))
    tarjeta_id = db.Column(db.Integer, db.ForeignKey('tarjeta.id'))
    tarjeta = db.relationship("Tarjeta", backref=db.backref("usuario", uselist=False))


class Tarjeta(db.Model):
    __tablename__ = 'tarjeta'
    id = db.Column(db.Integer, primary_key=True, autoincrement=False)
    puntos = db.Column(db.Integer)
    ubicacion_id = db.Column(db.Integer, db.ForeignKey('ubicacion.id'))
    ubicacion = db.relationship("Ubicacion")
    facturas = db.relationship("Factura")


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
    descripcion = db.Column(db.String(1000))
    valor = db.Column(db.Float)
    fecha = db.Column(db.TIMESTAMP(timezone=True))
    puntos = db.Column(db.Integer)
    tarjeta_id = db.Column(db.Integer, db.ForeignKey('tarjeta.id'))
    ubicacion_id = db.Column(db.Integer, db.ForeignKey('ubicacion.id'))

class Master(db.Model):
    __tablename__ = 'master'
    cedula = db.Column(db.Integer, primary_key=True, autoincrement=False)
    password = db.Column(db.String(100))
    ubicacion_id = db.Column(db.Integer, db.ForeignKey('ubicacion.id'))
    ubicacion = db.relationship('Ubicacion')
