from flask import render_template, request, jsonify
from app import app
from app.db import insert_review, get_reviews ,db
import pickle

# Load the sentiment analysis model
with open('models/sentiment_model.pkl', 'rb') as f:
    model = pickle.load(f)

@app.route('/')
def index():
    reviews = get_reviews()  # Retrieve reviews from the database
    return render_template('index.html', reviews=reviews)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.form['review']
    prediction = model.predict([data])[0]
    
    # Save the review and its sentiment to MongoDB
    insert_review(data, prediction)
    
    return jsonify({'sentiment': prediction})

# 🔁 Liveness Probe: Is the app running?
@app.route('/healthz', methods=['GET'])
def healthz():
    return jsonify({'status': 'alive'}), 200

# ✅ Readiness Probe: Is the app ready to serve traffic?
@app.route('/ready', methods=['GET'])
def ready():
    try:
        # Try to run a simple DB command
        db.command("ping")
        return jsonify({'status': 'ready'}), 200
    except Exception as e:
        return jsonify({'status': 'not ready', 'reason': str(e)}), 500
