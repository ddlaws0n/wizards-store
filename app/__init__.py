from flask import Flask

def create_app():
    app = Flask(__name__)

    # Import blueprints
    from .routes import main_blueprint, register_blueprint

    # Register blueprints
    app.register_blueprint(main_blueprint)
    app.register_blueprint(register_blueprint)

    return app
