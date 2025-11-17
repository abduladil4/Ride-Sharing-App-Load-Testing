from flask import Flask, jsonify, request
import random
import time

app = Flask(__name__)

# Sample drivers
drivers = [
    {"id": 1, "name": "Ravi", "rating": 4.8},
    {"id": 2, "name": "Akhil", "rating": 4.5},
    {"id": 3, "name": "Karan", "rating": 4.7},
    {"id": 4, "name": "John", "rating": 4.6},
]

@app.route("/search_ride", methods=["GET"])
def search_ride():
    pickup = request.args.get("pickup")
    drop = request.args.get("drop")

    time.sleep(random.uniform(0.1, 1.5))  # simulate server delay

    return jsonify({
        "status": "success",
        "pickup": pickup,
        "drop": drop,
        "available_drivers": drivers
    })

@app.route("/book_ride", methods=["POST"])
def book_ride():
    data = request.json
    driver = random.choice(drivers)

    return jsonify({
        "status": "ride booked",
        "driver": driver,
        "pickup": data["pickup"],
        "drop": data["drop"]
    })

@app.route("/complete_ride", methods=["POST"])
def complete_ride():
    data = request.json
    fare = random.randint(80, 500)

    return jsonify({
        "status": "completed",
        "ride_id": data.get("ride_id", random.randint(1000, 9999)),
        "fare": fare
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
