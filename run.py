from app import create_app
from app.users.views import users_bp
from app.products.views import products_bp

app = create_app()

# Register Blueprints
app.register_blueprint(users_bp)
app.register_blueprint(products_bp)

if __name__ == '__main__':
    app.run(debug=True)
