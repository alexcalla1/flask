from flask import Flask

def create_app():
    app = Flask(__name__)

    # Configuraciones opcionales, si las necesitas
    app.config.from_object('config.Config')

    # Importa y registra tus rutas aquí
    from app import routes
    app.register_blueprint(routes.bp)

    return app