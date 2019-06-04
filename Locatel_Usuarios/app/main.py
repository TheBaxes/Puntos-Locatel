from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_user, login_required, current_user, logout_user
from . import db
from .models import Usuario, Ubicacion

main = Blueprint('main', __name__)

@main.route("/")
def login():
    return render_template('LoginUsuario.html')


@main.route("/", methods=['POST'])
def login_post():
    cedula = request.form.get('cedula')
    password = request.form.get('pass')

    usuario = Usuario.query.filter_by(cedula=cedula).first()

    if not usuario or not usuario.password == password or not usuario.tarjeta:
        flash('Datos de ingreso erroneos el usuario no tiene una tarjeta Locatel activa.')
        return redirect(url_for('main.login'))

    login_user(usuario)
    
    return redirect(url_for('main.vista'))


def convertir(puntos, ratio_origen, ratio_destino, valor_origen, valor_destino):
    if ratio_origen == ratio_destino:
        return puntos
    ratio = ratio_origen / ratio_destino
    dinero = puntos * valor_origen
    dinero = dinero / ratio
    return int(dinero / valor_destino)

@main.route("/usuario")
@login_required
def vista():
    puntos = current_user.tarjeta.puntos
    ratio_origen = current_user.tarjeta.ubicacion.ratio
    valor_origen = current_user.tarjeta.ubicacion.valor_obtencion
    col = Ubicacion.query.filter_by(nombre="Colombia").first()
    usa = Ubicacion.query.filter_by(nombre="Estados Unidos").first()
    ven = Ubicacion.query.filter_by(nombre="Venezuela").first()
    col = convertir(puntos, ratio_origen, col.ratio, valor_origen, col.valor_obtencion)
    usa = convertir(puntos, ratio_origen, usa.ratio, valor_origen, usa.valor_obtencion)
    ven = convertir(puntos, ratio_origen, ven.ratio, valor_origen, ven.valor_obtencion)
    return render_template('VistaCliente.html', user=current_user, col=col, usa=usa, ven=ven)

@main.route("/convertir", methods=["POST"])
@login_required
def convertir_puntos_usuario():
    puntos = current_user.tarjeta.puntos
    ratio_origen = current_user.tarjeta.ubicacion.ratio
    valor_origen = current_user.tarjeta.ubicacion.valor_obtencion
    destino = request.form.get("Pais")
    destino = Ubicacion.query.filter_by(nombre=destino).first()
    puntos = convertir(puntos, ratio_origen, destino.ratio, valor_origen, destino.valor_obtencion)
    current_user.tarjeta.puntos = puntos
    current_user.tarjeta.ubicacion = destino
    db.session.commit()
    return redirect(url_for('.vista'))

@main.route("/catalogo")
@login_required
def catalogo():
    productos = current_user.tarjeta.ubicacion.productos
    valor_redencion = current_user.tarjeta.ubicacion.valor_redencion
    return render_template('CatalogoProductos.html', productos=productos, valor_redencion=valor_redencion)

@main.route("/historial")
@login_required
def historial():
    facturas = current_user.tarjeta.facturas
    return render_template('HistorialCompras.html', facturas=facturas)

@main.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.login'))
