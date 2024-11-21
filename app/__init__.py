from flask import Flask

def create_app():
    app = Flask(__name__)

    # Register routes here or in another file like routes.py
    from app.routes import main_routes
    app.register_blueprint(main_routes)

    return app