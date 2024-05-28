from flask import Blueprint, jsonify

users_bp = Blueprint('users', __name__)

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
