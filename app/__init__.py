from flask import Flask

# Initialize the Flask application
app = Flask(__name__)

# Import routes after app is initialized
from app import routes
