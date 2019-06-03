from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_user, login_required, current_user, logout_user
from . import db
from .models import Usuario

main = Blueprint('main', __name__)

@main.route("/")
def login():
    return render_template('LoginUsuario.html')


@main.route("/", methods=['POST'])
def login_post():
    cedula = request.form.get('cedula')
    password = request.form.get('pass')

    usuario = Usuario.query.filter_by(cedula=cedula).first()

    if not usuario or not usuario.password == password:
        flash('Datos de ingreso erroneos. ({}:{})'.format(cedula, password))
        return redirect(url_for('main.login'))

    login_user(usuario)
    
    return redirect(url_for('main.vista'))


@main.route("/usuario")
@login_required
def vista():
    return render_template('VistaCliente.html')

@main.route("/catalogo")
@login_required
def catalogo():
    return render_template('CatalogoProductos.html')

@main.route("/historial")
@login_required
def historial():
    return render_template('HistorialCompras.html')

@main.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.login'))
