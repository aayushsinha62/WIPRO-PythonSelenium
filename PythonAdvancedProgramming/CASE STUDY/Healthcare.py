from flask import Flask, jsonify, request

app = Flask(__name__)

# ----------------------------
# Simple Bearer Token Auth
# ----------------------------
VALID_TOKEN = "secret-token-123"

def authenticate():
    auth_header = request.headers.get("Authorization")
    if not auth_header or not auth_header.startswith("Bearer "):
        return False
    token = auth_header.split(" ")[1]
    return token == VALID_TOKEN


@app.before_request
def check_auth():
    if request.endpoint != "home":
        if not authenticate():
            return jsonify({"error": "Unauthorized"}), 401


@app.route("/")
def home():
    return "Healthcare Appointment Management API"


# ----------------------------
# In-memory databases
# ----------------------------
doctors = {}
patients = {}
appointments = {}

doctor_id_seq = 1
patient_id_seq = 1
appointment_id_seq = 1


# ----------------------------
# Doctor Creation
# ----------------------------
@app.route("/v1/doctors", methods=["POST"])
def create_doctor():
    global doctor_id_seq
    data = request.get_json()

    if not data or "name" not in data or "specialization" not in data:
        return jsonify({"error": "Invalid input"}), 400

    doctor = {
        "doctor_id": doctor_id_seq,
        "name": data["name"],
        "specialization": data["specialization"],
        "experience": data.get("experience", 0)
    }

    doctors[doctor_id_seq] = doctor
    doctor_id_seq += 1

    return jsonify(doctor), 201


# ----------------------------
# Patient Registration
# ----------------------------
@app.route("/v1/patients", methods=["POST"])
def register_patient():
    global patient_id_seq
    data = request.get_json()

    if not data or "name" not in data or "email" not in data or "phone" not in data:
        return jsonify({"error": "Missing required fields"}), 400

    if data.get("age", 0) < 0:
        return jsonify({"error": "Invalid age"}), 400

    # Duplicate phone check
    for patient in patients.values():
        if patient["phone"] == data["phone"]:
            return jsonify({"error": "Duplicate phone number"}), 409

    patient = {
        "patient_id": patient_id_seq,
        "name": data["name"],
        "email": data["email"],
        "phone": data["phone"],
        "age": data.get("age", 0)
    }

    patients[patient_id_seq] = patient
    patient_id_seq += 1

    return jsonify(patient), 201


# ----------------------------
# Book Appointment
# ----------------------------
@app.route("/v1/appointments", methods=["POST"])
def book_appointment():
    global appointment_id_seq
    data = request.get_json()

    required_fields = ["patient_id", "doctor_id", "date", "time"]
    if not all(field in data for field in required_fields):
        return jsonify({"error": "Invalid input"}), 400

    if data["patient_id"] not in patients or data["doctor_id"] not in doctors:
        return jsonify({"error": "Invalid patient or doctor ID"}), 400

    # Slot conflict check
    for appt in appointments.values():
        if (
            appt["doctor_id"] == data["doctor_id"]
            and appt["date"] == data["date"]
            and appt["time"] == data["time"]
            and appt["status"] == "BOOKED"
        ):
            return jsonify({"error": "Time slot already booked"}), 409

    appointment = {
        "appointment_id": appointment_id_seq,
        "patient_id": data["patient_id"],
        "doctor_id": data["doctor_id"],
        "date": data["date"],
        "time": data["time"],
        "status": "BOOKED"
    }

    appointments[appointment_id_seq] = appointment
    appointment_id_seq += 1

    return jsonify(appointment), 201


# ----------------------------
# View Appointment
# ----------------------------
@app.route("/v1/appointments/<int:id>", methods=["GET"])
def get_appointment(id):
    appointment = appointments.get(id)
    if not appointment:
        return jsonify({"error": "Appointment not found"}), 404

    return jsonify(appointment), 200


# ----------------------------
# Reschedule Appointment
# ----------------------------
@app.route("/v1/appointments/<int:id>", methods=["PUT"])
def reschedule_appointment(id):
    appointment = appointments.get(id)
    if not appointment:
        return jsonify({"error": "Appointment not found"}), 404

    data = request.get_json()
    new_date = data.get("date")
    new_time = data.get("time")

    # Check slot conflict
    for appt in appointments.values():
        if (
            appt["doctor_id"] == appointment["doctor_id"]
            and appt["date"] == new_date
            and appt["time"] == new_time
            and appt["status"] == "BOOKED"
        ):
            return jsonify({"error": "New time slot already booked"}), 409

    appointment["date"] = new_date
    appointment["time"] = new_time

    return jsonify(appointment), 200


# ----------------------------
# Cancel Appointment
# ----------------------------
@app.route("/v1/appointments/<int:id>", methods=["DELETE"])
def cancel_appointment(id):
    appointment = appointments.get(id)

    if not appointment:
        return jsonify({"error": "Appointment not found"}), 404

    if appointment["status"] == "CANCELLED":
        return jsonify({"error": "Appointment already cancelled"}), 410

    appointment["status"] = "CANCELLED"
    return "", 204


if __name__ == "__main__":
    app.run(debug=True)
