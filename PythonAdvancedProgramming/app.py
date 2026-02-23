# # flask - python web fw  - web apps , rest apis and microservices
# from flask import Flask
# from flask import Flask, jsonify, request
#
# # creates a flask object
# app = Flask(__name__)
#
#
# @app.route("/")
# def home():
#     return "Welcome to Flask web server!"
#
#
# # get method end point
# @app.route('/users', methods=['GET'])
# def get_users():
#     return jsonify({"users": ["Alice", "Bob", "Charlie"]})
#
#
# # post method end point
# @app.route('/users', methods=['POST'])
# def add_users():
#     data = request.get_json()
#     return jsonify(data), 201
#
#
# # put request
# @app.route('/users/<int:id>', methods=['PUT'])
# def update_users(id):
#     return jsonify({"Message": f"user {id} is updated"})
#
#
# @app.route('/users/<int:id>', methods=['DELETE'])
# def delete_user(id):
#     return jsonify({"message": f"User {id} deleted"})
#
#
# @app.route('/users/<int:id>', methods=['PATCH'])
# def patch_user(id):
#     data = request.get_json()
#     return jsonify({
#         "message": "User updated partially",
#         "user_id": id,
#         "updated_fields": data
#     })
#
#
# #  run the below  code only if this file is executed directly and not when imported
# if __name__ == "__main__":
#     app.run(debug=True)
# # run the local server - 127.0.0.1 or localhost:5000
# # enable the debugging  mode
#
#
#
#
#
#
#
#
#
#
from flask import Flask, jsonify, request

app = Flask(__name__)

# -------------------- In-Memory Database --------------------
users = []
next_user_id = 1   # Auto-increment ID


# -------------------- Home --------------------
@app.route("/")
def home():
    return "Welcome to Flask REST API 🚀"


# -------------------- GET --------------------
# Get all users
@app.route("/users", methods=["GET"])
def get_users():
    return jsonify(users), 200


# Get user by ID
@app.route("/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    for user in users:
        if user["id"] == user_id:
            return jsonify(user), 200
    return jsonify({"error": "User not found"}), 404


# -------------------- POST --------------------
# Create a new user
@app.route("/users", methods=["POST"])
def create_user():
    global next_user_id

    data = request.get_json()

    if not data or "name" not in data or "age" not in data:
        return jsonify({"error": "name and age are required"}), 400

    new_user = {
        "id": next_user_id,     # ID generated here
        "name": data["name"],
        "age": data["age"]
    }

    users.append(new_user)
    next_user_id += 1

    return jsonify(new_user), 201


# -------------------- PUT --------------------
# Replace an entire user
@app.route("/users/<int:user_id>", methods=["PUT"])
def update_user(user_id):
    data = request.get_json()

    if not data or "name" not in data or "age" not in data:
        return jsonify({"error": "name and age are required"}), 400

    for user in users:
        if user["id"] == user_id:
            user["name"] = data["name"]
            user["age"] = data["age"]
            return jsonify(user), 200

    return jsonify({"error": "User not found"}), 404


# -------------------- PATCH --------------------
# Partially update a user
@app.route("/users/<int:user_id>", methods=["PATCH"])
def patch_user(user_id):
    data = request.get_json()

    if not data:
        return jsonify({"error": "No data provided"}), 400

    for user in users:
        if user["id"] == user_id:
            if "name" in data:
                user["name"] = data["name"]
            if "age" in data:
                user["age"] = data["age"]
            return jsonify(user), 200

    return jsonify({"error": "User not found"}), 404


# -------------------- DELETE --------------------
# Delete a user
@app.route("/users/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    for user in users:
        if user["id"] == user_id:
            users.remove(user)
            return jsonify({"message": "User deleted successfully"}), 200

    return jsonify({"error": "User not found"}), 404


# -------------------- Run Server --------------------
if __name__ == "__main__":
    app.run(debug=True)



if __name__ == "__main__":
    app.run(debug=True)

