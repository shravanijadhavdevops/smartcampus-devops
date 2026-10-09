
import os
from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

students = [
    {"id": 1, "name": "Aarav Sharma", "course": "Cloud Computing"},
    {"id": 2, "name": "Priya Patil", "course": "DevOps Engineering"},
]

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/health")
def health():
    return jsonify({
        "status": "healthy",
        "application": "SmartCampus",
        "version": os.getenv("APP_VERSION", "1.0.0")
    }), 200

@app.route("/api/students", methods=["GET"])
def get_students():
    return jsonify(students), 200

@app.route("/api/students", methods=["POST"])
def add_student():
    data = request.get_json(silent=True) or {}
    name = data.get("name", "").strip()
    course = data.get("course", "").strip()

    if not name or not course:
        return jsonify({"error": "Name and course are required"}), 400

    student = {
        "id": max((s["id"] for s in students), default=0) + 1,
        "name": name,
        "course": course,
    }
    students.append(student)
    return jsonify(student), 201

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
