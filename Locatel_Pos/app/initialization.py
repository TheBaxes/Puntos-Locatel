from . import db
from .models import *


def init_db():
    productos = [Producto(nombre="Producto 1", imagen=("imagen1.png")),
                 Producto(nombre="Producto 2", imagen=("imagen2.png")),
                 Producto(nombre="Producto 3", imagen=("imagen3.png")),
                 Producto(nombre="Producto 4", imagen=("imagen4.png")),
                 Producto(nombre="Producto 5", imagen=("imagen5.png"))
    ]
    producto_precio = [Producto_Ubicacion(precio=1000.0),
                       Producto_Ubicacion(precio=2000.0),
                       Producto_Ubicacion(precio=30000.0),
                       Producto_Ubicacion(precio=10500.0),
                       Producto_Ubicacion(precio=5200.0),
    ]
    for a, b in zip(producto_precio, productos):
        a.producto = b
    ubicacion = Ubicacion(nombre="colombia", valor_obtencion=200.0, valor_redencion=0.5)
    for a in producto_precio:
        ubicacion.productos.append(a)
    tarjeta = Tarjeta(id=1234, puntos = 0, ubicacion=ubicacion)
    usuario = Usuario(cedula=123456, nombre="Pepe", password="xdxdxd", tarjeta=tarjeta)
    master = Master(cedula=4321, password="xdxdxd", ubicacion=ubicacion)
    for a in productos:
        db.session.add(a)
    for a in producto_precio:
        db.session.add(a)
    db.session.add(ubicacion)
    db.session.add(tarjeta)
    db.session.add(usuario)
    db.session.commit()
