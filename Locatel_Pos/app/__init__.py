# Import flask and template operators
from flask import Flask, render_template
#from flask_login import LoginManager


# Import SQLAlchemy
from flask_sqlalchemy import SQLAlchemy

# Define the WSGI application object
app = Flask(__name__)

# Configurations
app.config.from_object('config')
app.jinja_env.filters['zip'] = zip

# Define the database object which is imported
# by modules and controllers
db = SQLAlchemy(app)

# login_manager = LoginManager()
# login_manager.login_view = 'main.login'
# login_manager.init_app(app)

# from .models import Master

# @login_manager.user_loader
# def load_master(master_id):
#     return Master.query.get(int(master_id))

# Sample HTTP error handling
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404


# Import a module / component using its blueprint handler variable (mod_auth)
from .main import main as main_blueprint
from .country import country as country_blueprint

# Register blueprint(s)
app.register_blueprint(main_blueprint)
app.register_blueprint(country_blueprint)

#from .models import *

# Build the database:
# This will create the database file using SQLAlchemy
db.create_all()
