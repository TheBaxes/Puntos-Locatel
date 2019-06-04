from flask import Blueprint, render_template, request, session, url_for, redirect
from .initialization import init_db

country = Blueprint('country', __name__, url_prefix='/country')

def set_cookie(country):
    session['country'] = country
    return redirect(url_for('main.venta_pos'))

@country.route('/colombia')
def colombia():
    return set_cookie('Colombia')

@country.route('/venezuela')
def venezuela():
    return set_cookie('Venezuela')

@country.route('/usa')
def usa():
    return set_cookie('Estados Unidos')
