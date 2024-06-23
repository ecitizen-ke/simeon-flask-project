from flask import Blueprint, request, jsonify, session
from app.models import User

main = Blueprint('main', __name__)

@main.route('/')
def home():
    if 'username' in session:
        return jsonify({"message": f"Welcome, {session['username']}"}), 200
    return jsonify({"message": "Please log in"}), 401

@main.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    user = User()
    if user.user_login(username, password):
        session['username'] = username
        return jsonify({"message": "Login successful"}), 200
    return jsonify({"message": "Invalid username or password"}), 401

@main.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    user = User()
    user.create(username, password)
    return jsonify({"message": "Registration successful"}), 201

@main.route('/logout')
def logout():
    session.pop('username', None)
    return jsonify({"message": "Logged out successfully"}), 200
