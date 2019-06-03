from . import db
from models import *


def init_db():
    producto = [Producto(nombre="caja")]
    producto_precio = Producto_Ubicacion(precio=10.0)
    producto_precio.producto = productos[0]
    ubicacion = Ubicacion(nombre="Rusia", valor_obtencion=1.0, valor_redencion=0.5)
    ubicacion.productos.append(producto_precio)
    usuario = Usuario(cedula=1234, nombre="Pepe", puntos=0, ubicacion_id=ubicacion)
    db.session.add(producto)
    db.session.add(producto_precio)
    db.session.add(ubicacion)
    db.session.add(usuario)
    db.session.commit()
