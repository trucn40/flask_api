from flask import Flask
from config import config_by_name

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config_by_name[config_name])

    from .routes import api_blueprint
    app.register_blueprint(api_blueprint, url_prefix='/api')

    return app
