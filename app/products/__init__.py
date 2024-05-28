from flask import Blueprint, jsonify

products_bp = Blueprint('products', __name__)

@products_bp.route('/products')
def get_products():
    product_data = {
        "products": {
            "fruits": ["apple", "banana", "mango"],
            "beverages": ["coffee", "tea", "coca-cola"]
        }
    }
    return jsonify(product_data)
