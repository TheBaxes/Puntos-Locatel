from . import db
from .models import *


def init_db():
    productos = [Producto(nombre="Producto 1", imagen=("imagen1.png")),
                 Producto(nombre="Producto 2", imagen=("imagen2.png")),
                 Producto(nombre="Producto 3", imagen=("imagen3.png")),
                 Producto(nombre="Producto 4", imagen=("imagen4.png")),
                 Producto(nombre="Producto 5", imagen=("imagen5.png"))
    ]
    precio_colombia = [Producto_Ubicacion(precio=1000.0),
                       Producto_Ubicacion(precio=2000.0),
                       Producto_Ubicacion(precio=30000.0),
                       Producto_Ubicacion(precio=10500.0),
                       Producto_Ubicacion(precio=5200.0),
    ]
    precio_ven = [Producto_Ubicacion(precio=10000000.0),
                  Producto_Ubicacion(precio=20000000.0),
                  Producto_Ubicacion(precio=300000000.0),
                  Producto_Ubicacion(precio=105000000.0),
                  Producto_Ubicacion(precio=52000000.0),
    ]
    for a, b in zip(precio_colombia, productos):
        a.producto = b
    for a, b in zip(precio_ven, productos):
        a.producto = b
    colombia = Ubicacion(nombre="Colombia", valor_obtencion=200.0, valor_redencion=0.5, codigo="COP", ratio=3000.0)
    for a in precio_colombia:
        colombia.productos.append(a)
    ven = Ubicacion(nombre="Venezuela", valor_obtencion=2000000.0, valor_redencion=0.00005, codigo="VES", ratio=20000.0)
    for a in precio_ven:
        ven.productos.append(a)
    usa = Ubicacion(nombre="Estados Unidos", valor_obtencion=0.1, valor_redencion=0.01, codigo="USA", ratio=1.0)
    tarjeta = Tarjeta(id=1234, puntos=200, ubicacion=colombia)
    usuario = Usuario(cedula=123456, nombre="Pepe", password="xdxdxd", tarjeta=tarjeta)
    master_co = Master(cedula=4321, password="xdxdxd", ubicacion=colombia)
    master_ve = Master(cedula=6789, password="xdxdxd", ubicacion=ven)
    master_us = Master(cedula=123, password="xdxdxd", ubicacion=usa)
    for a in productos:
        db.session.add(a)
    for a in precio_colombia:
        db.session.add(a)
    for a in precio_ven:
        db.session.add(a)
    db.session.add(colombia)
    db.session.add(ven)
    db.session.add(usa)
    db.session.add(tarjeta)
    db.session.add(usuario)
    db.session.add(master_co)
    db.session.add(master_ve)
    db.session.add(master_us)
    db.session.commit()
