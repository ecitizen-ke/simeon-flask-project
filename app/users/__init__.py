from flask import jsonify

def view_users(my_app):
    @my_app.route('/users')
    def get_users():
        # Dictionary definition
        user_data = {
            "users": [
                {"username": "firstUser", "password" : "firstPassowrd"},
                {"username": "secondUser", "password" : "secondPassowrd"},
                {"username": "thirdUser", "password" : "thirdPassowrd"}
            ]
        }
    # returning the dictionary as a JSON response
        return jsonify(user_data)
    
