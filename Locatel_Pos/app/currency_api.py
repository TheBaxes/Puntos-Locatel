from flask import Blueprint
from .models import Ubicacion

currency_api = Blueprint('currency_api', __name__, url_prefix="/currency")

@currency_api.route("/update")
def update():
    monedas = Ubicacion.query.all()
