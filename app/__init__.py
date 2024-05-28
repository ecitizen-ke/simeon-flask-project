from flask import Flask

def create_app():
    app = Flask(__name__)

    from .users import users_bp
    from .products import products_bp

    app.register_blueprint(users_bp)
    app.register_blueprint(products_bp)

    return app
