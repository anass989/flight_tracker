from flask import Flask
from flask_bootstrap import Bootstrap
# from gather_data import gather_data

app = Flask(__name__, static_folder="static", template_folder="templates")
Bootstrap(app)
app.config['TEMPLATES_AUTO_RELOAD'] = True

# app.register_blueprint(gather_data)

from app import views
