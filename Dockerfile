# Use the official Python image as a base
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt /app/

# Install python3-dev and other necessary packages
RUN apt-get update && apt-get install -y python3-dev

# Install distutils
RUN apt-get update && apt-get install -y python3-distutils

# Install the dependencies from the requirements.txt file
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire application code into the container
COPY . /app/

# Expose the port the app runs on (default Flask port)
EXPOSE 5000

# Set the environment variable for Flask
ENV FLASK_APP=run.py
ENV FLASK_ENV=development

# Run the Flask app using Flask's built-in server
CMD ["flask", "run", "--host=0.0.0.0"]
