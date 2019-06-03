from flask import Blueprint, render_template, request
from .initialization import init_db

main = Blueprint('main', __name__)


@main.route("/pos")
def consulta_venta_pos():
    return render_template('VistaPos.html')

@main.route("/")
def seleccion_pais():
    return render_template('PosInicial.html')

@main.route("/ventaPos")
def venta_pos():
    return render_template('VentaPos.html')
@main.route("/tarjeta")
def pago_pos():
    return render_template('PagoTarjeta.html')

@main.route("/detalles")
def detalles_puntos():
    return render_template('DetallesPuntos.html')

@main.route("/init_db")
def init():
    init_db()
    return "Database initialized"
