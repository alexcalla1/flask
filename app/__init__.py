from flask import Flask
from app.routes import predicciones_bp

def create_app():
    app = Flask(__name__)

    # Configuraciones opcionales, si las necesitas
    app.config.from_object('config.Config')

    # Registra el Blueprint
    app.register_blueprint(predicciones_bp)

    return app