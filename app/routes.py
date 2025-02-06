from flask import render_template, request, jsonify
from app import app
from app.db import insert_review, get_reviews
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
