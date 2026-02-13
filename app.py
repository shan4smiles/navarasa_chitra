from flask import Flask, render_template, request, jsonify, send_from_directory
from flask_cors import CORS
import json
import os
from datetime import datetime

app = Flask(__name__, static_folder='static', template_folder='templates')
CORS(app)

DATA_FILE = 'data/mandala_state.json'

# Ensure data file exists
if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, 'w') as f:
        json.dump([], f)

def get_state():
    try:
        if os.path.getsize(DATA_FILE) == 0:
            return []
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    except (json.JSONDecodeError, FileNotFoundError):
        return []

def save_entry(entry):
    state = get_state()
    state.append(entry)
    with open(DATA_FILE, 'w') as f:
        json.dump(state, f, indent=4)

@app.route('/')
def participant_ui():
    return render_template('index.html')

@app.route('/mandala_display')
def live_display():
    return render_template('mandala.html')

@app.route('/submit', methods=['POST'])
def submit():
    data = request.json
    # Expected: { petals: [ { rasa: '', color: '', element: '' }, ... ] }
    petals = data.get('petals', [])
    if not petals:
        return jsonify({"status": "error", "message": "No petals provided"}), 400
        
    entry = {
        "id": datetime.now().strftime("%Y%m%d%H%M%S"),
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "petals": petals
    }
    save_entry(entry)
    return jsonify({"status": "success", "total_rings": len(get_state())})

@app.route('/state')
def state():
    return jsonify(get_state())

if __name__ == '__main__':
    print("Navarasa Chitra Server Starting...")
    print("Participant UI: http://localhost:5001")
    print("Live Mandala Display: http://localhost:5001/mandala_display")
    app.run(port=5001, debug=True)
