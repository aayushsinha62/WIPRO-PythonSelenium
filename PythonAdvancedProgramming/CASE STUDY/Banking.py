# flask - python web fw  - web apps , rest apis and microservices
from flask import Flask, jsonify, request

# creates a flask object
app = Flask(__name__)

# ----------------------------
# In-memory database
# ----------------------------
customers = {}
current_id = 1


@app.route("/")
def home():
    return "Welcome to Bank Customer API!"


# ----------------------------
# POST – Create Customer
# ----------------------------
@app.route('/customers', methods=['POST'])
def create_customer():
    global current_id

    data = request.get_json()

    if not data or "name" not in data or "email" not in data:
        return jsonify({"error": "Invalid input"}), 400

    customer = {
        "id": current_id,
        "name": data["name"],
        "email": data["email"],
        "balance": data.get("balance", 0)
    }

    customers[current_id] = customer
    current_id += 1

    return jsonify(customer), 201


# ----------------------------
# GET – Retrieve Customer
# ----------------------------
@app.route('/customers/<int:id>', methods=['GET'])
def get_customer(id):
    customer = customers.get(id)

    if not customer:
        return jsonify({"error": "Customer not found"}), 404

    return jsonify(customer), 200


# ----------------------------
# PUT – Update Customer
# ----------------------------
@app.route('/customers/<int:id>', methods=['PUT'])
def update_customer(id):
    customer = customers.get(id)

    if not customer:
        return jsonify({"error": "Customer not found"}), 404

    data = request.get_json()

    if "email" in data:
        customer["email"] = data["email"]

    return jsonify(customer), 200


# ----------------------------
# DELETE – Remove Customer
# ----------------------------
@app.route('/customers/<int:id>', methods=['DELETE'])
def delete_customer(id):
    if id not in customers:
        return jsonify({"error": "Customer not found"}), 404

    del customers[id]
    return "", 204



if __name__ == "__main__":
    app.run(debug=True)
