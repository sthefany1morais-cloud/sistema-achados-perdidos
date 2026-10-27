from flask import Flask
from config import Config
from extensions import redis_client
from routes.main import main_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    redis_client.init_app(app)
    app.register_blueprint(main_bp)

    @app.template_filter("datetime")
    def format_datetime(value):
        from datetime import datetime
        try:
            return datetime.fromtimestamp(float(value)).strftime("%d/%m/%Y %H:%M")
        except (TypeError, ValueError, OSError):
            return "Data não informada"

    return app
