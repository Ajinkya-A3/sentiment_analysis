# Stage 1: Build stage
FROM python:3.10-slim AS builder

# Set the working directory
WORKDIR /app

# Install system dependencies required for building Python packages
RUN apt-get update && apt-get install -y python3-dev python3-distutils gcc

# Copy requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir --prefix=/install -r requirements.txt

# Stage 2: Runtime stage
FROM python:3.10-slim

# Set the working directory
WORKDIR /app

# Copy only the installed dependencies from the builder stage
COPY --from=builder /install /usr/local

# Copy the application code
COPY . /app/

# Expose the port
EXPOSE 5000

# Set environment variables
ENV FLASK_APP=run.py
ENV FLASK_ENV=development

# Run the Flask app
CMD ["flask", "run", "--host=0.0.0.0"]
