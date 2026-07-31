#!/usr/bin/python3
"""A simple API built with Flask."""
from flask import Flask, jsonify, request

app = Flask(__name__)

users = {}


@app.route("/")
def home():
    """Return the welcome message of the API."""
    return "Welcome to the Flask API!"


@app.route("/status")
def status():
    """Return the status of the API."""
    return "OK"


@app.route("/data")
def data():
    """Return the list of all the usernames stored in the API."""
    return jsonify(list(users.keys()))


@app.route("/users/<username>")
def get_user(username):
    """Return the full object matching the given username."""
    user = users.get(username)
    if user is None:
        return jsonify({"error": "User not found"}), 404
    return jsonify(user)


@app.route("/add_user", methods=["POST"])
def add_user():
    """Add a new user to the API from a JSON body."""
    payload = request.get_json(silent=True)
    if payload is None:
        return jsonify({"error": "Invalid JSON"}), 400
    username = payload.get("username")
    if not username:
        return jsonify({"error": "Username is required"}), 400
    if username in users:
        return jsonify({"error": "Username already exists"}), 409
    users[username] = payload
    return jsonify({"message": "User added", "user": payload}), 201


if __name__ == "__main__":
    app.run()
