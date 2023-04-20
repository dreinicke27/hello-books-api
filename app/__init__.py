from flask import Flask
from flask import Blueprint, jsonify

def create_app(test_config=None):
    app = Flask(__name__)

    from .routes import hello_world_bp
    app.register_blueprint(hello_world_bp)

    from .routes import books_bp
    app.register_blueprint(books_bp)

    return app