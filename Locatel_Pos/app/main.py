from flask import Blueprint, render_template, request

main = Blueprint('main', __name__)


@main.route("/")
def Consulta_venta_pos():
    return render_template('VistaPos.html')
