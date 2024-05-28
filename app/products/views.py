from . import products_bp
from flask import jsonify

@products_bp.route('/products')
def get_products():
    product_data = {
        "products": {
            "fruits": ["apple", "banana", "mango"],
            "beverages": ["coffee", "tea", "coca-cola"]
        }
    }
    return jsonify(product_data)
