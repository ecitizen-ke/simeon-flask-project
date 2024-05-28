from flask import jsonify

def view_products(app):
    @app.route('/products')
    def get_products():
        # Defining a dictionary with some product categories and items
        product_data = {
            "products" :{
                "fruits" : ["apple", "banana", "mango"],
                "beverages" : ["coffee", "tea", "cocacola"]
            }
        }
        # returning the dictionary as a JSON response
        return jsonify(product_data)