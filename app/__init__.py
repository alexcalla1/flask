from flask import Flask
from app.routes import bp as routes_bp  # Importa directamente el Blueprint

def create_app():
    app = Flask(__name__)

    # Configuraciones opcionales, si las necesitas
    app.config.from_object('config.Config')

    # Registra el Blueprint
    app.register_blueprint(routes_bp)

    return app
