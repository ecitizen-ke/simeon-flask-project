from flask import Flask, jsonify
from app.users import view_users
from app.products import view_products
app = Flask(__name__)

# view 2
view_users(app)

# view 3
view_products(app)

if __name__ == '__main__':
    app.run(debug=True)