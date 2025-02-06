from pymongo import MongoClient
from config import MONGO_URI

# Connect to MongoDB
client = MongoClient(MONGO_URI)
db = client.sentiment_analysis  # Database name
reviews_collection = db.reviews  # Collection name

def insert_review(review, sentiment):
    """Insert a new review into the database."""
    review_data = {"review": review, "sentiment": sentiment}
    reviews_collection.insert_one(review_data)

def get_reviews():
    """Retrieve all reviews from the database."""
    return list(reviews_collection.find({}, {"_id": 0}))
