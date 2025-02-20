# Sentiment Analysis with NLP and Machine Learning


# Project Directory Structure
```
sentiment_analysis/
├── data/
│   └── sample_reviews.csv   <-- Your CSV file with review data
├── models/
│   └── sentiment_model.pkl  <-- The trained model (this will be saved by the code)
├── app/
│   ├── __init__.py
│   ├── routes.py
│   ├── sentiment_model.py
│   └── db.py
├── config.py
├── run.py
├── requirements.txt
├── Dockerfile
├── mongo-setup.yaml  <-- MongoDB setup file for initialization
├── complete-app.yaml  <-- Complete app setup file 
├── .gitignore
└── .dockerignore
```



here application with docker compose file for mongodb setup is provided

you will need to use different connection url for different conditions
1.if you are using mongodb and mongoexpress in container and externally accessing the app 
2.else if you are using image built through Dockerfile and docker compose for starting those 3 images simultaneously 

If you prefer to use a local MongoDB instance:

Make sure MongoDB is running on your machine.
Modify the MongoDB connection URL in config.py with the correct connection string for your local MongoDB instance.

eg. MONGO_URI = "mongodb://localhost:27017/sentiment_analysis"

you can check the config file for further clarity

------------------------------------------------------------------------------------------------------
Prerequisites
1.Docker and Docker Compose installed on your machine.
2.Python 3.x and required libraries for local testing (if not using Docker).
3.MongoDB instance (for storing sentiment analysis results).

------------------------------------------------------------------------------------------------------

Docker commands to run the project

# to setup mongodb and mongo-express containers only 
docker-compose -f mongo-setup.yaml up

# to stop all containers
docker-compose -f mongo-setup.yaml down


# to start complete app in docker 
docker-compose -f complete-app.yaml up

# to stop all containers
docker-compose -f complete-app.yaml down
