from flask import Flask, jsonify
import random

app = Flask(__name__)

# Home page
@app.route("/")
def home():
    return jsonify({
        "message": "Weather API is running",
        "endpoints": [
            "/temperature/<location>",
            "/wind/<location>"
        ]
    })

# Temperature endpoint
@app.route("/temperature/<location>")
def temperature(location):
    return jsonify({
        "location": location,
        "temperature": random.randint(5, 25),
        "unit": "Celsius"
    })

# Wind endpoint
@app.route("/wind/<location>")
def wind(location):
    return jsonify({
        "location": location,
        "wind_speed": random.randint(1, 30),
        "unit": "kts",
        "direction": f"{random.randint(0,359):03d}deg"
    })

if __name__ == "__main__":
    app.run(debug=True)