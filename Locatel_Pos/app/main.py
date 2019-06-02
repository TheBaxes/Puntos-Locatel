from flask import Blueprint, render_template, request
from .initialization import init_db

main = Blueprint('main', __name__)


@main.route("/pos")
def Consulta_venta_pos():
    return render_template('VistaPos.html')

@main.route("/")
def Seleccion_pais():
    return render_template('PosInicial.html')

@main.route("/init_db")
def init():
    init_db()
    return "Database initialized"
