from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_user, login_required, current_user, logout_user
from . import db
from .models import Master

main = Blueprint('main', __name__)


@main.route("/")
def login():
    return render_template('MasterLogin.html')


@main.route("/", methods=['POST'])
def login_post():
    cedula = request.form.get('cedula')
    password = request.form.get('pass')

    master = Master.query.filter_by(cedula=cedula).first()

    if not master or not master.password == password:
        flash('Datos de ingreso erroneos. ({}:{})'.format(cedula, password))
        return redirect(url_for('main.login'))

    login_user(master)
    
    return redirect(url_for('main.vista'))


@main.route("/master", methods=['GET'])
@login_required
def vista():    
    return render_template('MasterVista.html', master=current_user)

@main.route("/master", methods=['POST'])
@login_required
def update():
    valor_obtencion = request.form.get('valor_obtencion')
    valor_redencion = request.form.get('valor_redencion')
    current_user.ubicacion.valor_obtencion = valor_obtencion
    current_user.ubicacion.valor_redencion = valor_redencion
    db.session.commit()
    return redirect(url_for('main.vista'))

@main.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.login'))
