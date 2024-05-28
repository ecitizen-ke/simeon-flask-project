from . import users_bp
from flask import jsonify

@users_bp.route('/users')
def get_users():
    user_data = {
        "users": [
            {"username": "firstUser", "password": "firstPassword"},
            {"username": "secondUser", "password": "secondPassword"},
            {"username": "thirdUser", "password": "thirdPassword"}
        ]
    }
    return jsonify(user_data)
