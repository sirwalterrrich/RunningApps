from flask import Flask, render_template, request, jsonify
import os

app = Flask(__name__)

# Ensure the sound files are in a folder named 'static'
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.get_json()
    distance_km = float(data['distance'])  # Distance in km
    time_seconds = float(data['time'])  # Total time in seconds
    time_minutes = time_seconds / 60  # Convert time to minutes

    # Handle case where distance is 0 to avoid division by zero
    if distance_km > 0:
        # Calculate pace in min/km
        pace_km = time_minutes / distance_km
        # Convert pace to min/mile
        pace_miles = pace_km * 1.60934
    else:
        pace_km = float('inf')  # Set to infinity if distance is 0
        pace_miles = float('inf')

    # Speed calculation in miles/hour
    speed = (distance_km * 0.621371) / (time_minutes / 60) if time_minutes > 0 else 0  # Avoid division by zero

    # Predict race times for common distances
    predictions = {
        '5k': pace_km * 5,
        '10k': pace_km * 10,
        'half_marathon': pace_km * 21.0975,
        'marathon': pace_km * 42.195
    }

    return jsonify({
        'pace_km': round(pace_km, 2) if pace_km != float('inf') else 'N/A',
        'pace_miles': round(pace_miles, 2) if pace_miles != float('inf') else 'N/A',
        'speed': round(speed, 2),
        'predictions': {key: round(value, 2) for key, value in predictions.items()}
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
