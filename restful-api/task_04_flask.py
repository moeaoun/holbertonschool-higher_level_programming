#!/usr/bin/env python3
"""Flask RESTful API with basic routing, JSON serving, and POST handling."""

from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory storage for users
users = {}

@app.route('/')
def home():
    """Root endpoint returning a welcome message."""
    return "Welcome to the Flask API!"

@app.route('/data')
def get_usernames():
    """Return list of all usernames stored in the API."""
    return jsonify(list(users.keys()))

@app.route('/status')
def status():
    """Return OK status."""
    return "OK"

@app.route('/users/<username>')
def get_user(username):
    """Return user object by username, or error if not found."""
    user = users.get(username)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404

@app.route('/add_user', methods=['POST'])
def add_user():
    """Add a new user with username, name, age, and city."""
    data = request.get_json()

    if not data or "username" not in data:
        return jsonify({"error": "Username is required"}), 400

    username = data["username"]
    user_data = {
        "username": username,
        "name": data.get("name", ""),
        "age": data.get("age", 0),
        "city": data.get("city", "")
    }
    users[username] = user_data

    return jsonify({
        "message": "User added",
        "user": user_data
    }), 201

if __name__ == "__main__":
    app.run()

