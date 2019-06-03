from functools import wraps
from flask import Blueprint, render_template, request, session, redirect, url_for, flash
from .initialization import init_db
from .models import Ubicacion, Producto_Ubicacion, Tarjeta

main = Blueprint('main', __name__)

def country_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'country' not in session:
            return redirect(url_for('.seleccion_pais'))
        return f(*args, **kwargs)
    return decorated_function


def compra_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'compra.total' not in session:
            return redirect(url_for('.venta_pos'))
        return f(*args, **kwargs)
    return decorated_function


@main.route("/pos", methods=["POST"])
@country_required
def consulta_venta_pos():
    compra = [Producto_Ubicacion.query.filter_by(id=x).first() for x in request.form.getlist('compra')]
    if len(compra) == 0:
        flash("No se seleccionaron productos.")
        return redirect(url_for('.venta_pos'))
    productos = ''
    precios = ''
    total = 0.0
    for relacion in compra:
        productos += relacion.producto.nombre + ','
        precios += str(relacion.precio) + ','
        total += relacion.precio
    productos = productos[:-1]
    precios = precios[:-1]
    session['compra.productos'] = productos
    session['compra.precios'] = precios
    session['compra.total'] = total
    ubicacion = Ubicacion.query.filter_by(nombre=session['country']).first()
    return render_template('VistaPos.html', productos=zip(productos.split(','), precios.split(',')), total=total, ubicacion=ubicacion)

@main.route("/pos", methods=["GET"])
@country_required
@compra_required
def consulta_venta_pos_again():
    productos = session['compra.productos']
    precios = session['compra.precios']
    total = float(session['compra.total'])
    ubicacion = Ubicacion.query.filter_by(nombre=session['country']).first()
    return render_template('VistaPos.html', productos=zip(productos.split(','), precios.split(',')), total=total, ubicacion=ubicacion)

@main.route("/finCompra")
@country_required
def fin_compra():
    session.pop('compra.productos', None)
    session.pop('compra.precios', None)
    session.pop('compra.total', None)
    return redirect(url_for('.venta_pos'))

@main.route("/finCompra", methods=["POST"])
@country_required
@compra_required
def pago_puntos():
    total = float(session['compra.total'])
    puntos_usados = request.form.get('pointsToUse')
    tarjeta = Tarjeta.query.filter_by(id=session['tarjeta']).first()
    session.pop('compra.productos', None)
    session.pop('compra.precios', None)
    session.pop('compra.total', None)
    return redirect(url_for('.venta_pos'))

@main.route("/")
def seleccion_pais():
    return render_template('PosInicial.html')

@main.route("/ventaPos")
@country_required
def venta_pos():
    ubicacion = Ubicacion.query.filter_by(nombre=session['country']).first()
    return render_template('VentaPos.html', productos=ubicacion.productos)

@main.route("/tarjeta")
@country_required
@compra_required
def pago_pos():
    return render_template('PagoTarjeta.html')

@main.route("/detalles", methods=["POST"])
@country_required
@compra_required
def detalles_puntos():
    ntarjeta = request.form.get('tarjeta')
    tarjeta = Tarjeta.query.filter_by(id=ntarjeta).first()
    if not tarjeta:
        flash("No se encontro el número de la tarjeta Locatel.")
        return redirect(url_for('.consulta_venta_pos_again'))
    session['tarjeta'] = tarjeta.id
    return render_template('DetallesPuntos.html', total=session['compra.total'], tarjeta=tarjeta)

@main.route("/init_db")
def init():
    init_db()
    return "Database initialized"
