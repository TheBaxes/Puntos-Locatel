from flask_login import UserMixin
from . import db


class Master(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cedula = db.Column(db.Integer, unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
