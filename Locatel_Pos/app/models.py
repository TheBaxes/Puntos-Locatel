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
    puntos = db.Column(db.Integer)
    ubicacion_id = db.Column(db.Integer, db.ForeignKey('ubicacion.id'))
    ubicacion = db.relationship("Ubicacion")

class Producto(db.Model):
    __tablename__ = 'producto'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100))


class Producto_Ubicacion(db.Model):
    __tablename__ = 'producto_ubicacion'
    ubicacion_id = db.Column(db.Integer, db.ForeignKey('ubicacion.id'),
                             primary_key=True)
    producto_id = db.Column(db.Integer, db.ForeignKey('producto.id'),
                            primary_key=True)
    precio = db.Column(db.Float)
    producto = db.relationship("Producto")


class Factura(db.Model):
    __tablename__ = 'factura'
    id = db.Column(db.Integer, primary_key=True)
    descripcion = db.Column(db.String(1000))
    valor = db.Column(db.Float)
    fecha = db.Column(db.TIMESTAMP(timezone=True))
    puntos = db.Column(db.Integer)
    cedula_id = db.Column(db.Integer, db.ForeignKey('usuario.cedula'))
    ubicacion_id = db.Column(db.Integer, db.ForeignKey('ubicacion.id'))
