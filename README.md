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

#Docker commands to run the project

to setup mongodb and mongo-express containers only
```
docker-compose -f mongo-setup.yaml up
```

to stop all containers
```
docker-compose -f mongo-setup.yaml down
```

to start complete app in docker
```
docker-compose -f complete-app.yaml up
```
to stop all containers
```
docker-compose -f complete-app.yaml down
```


# Flask CI/CD Pipeline with GitHub Actions, Docker and Argo CD

This repository demonstrates a complete CI/CD pipeline for a Flask application using:

- **GitHub Actions** for Continuous Integration
- **Trivy** and **Gitleaks** for security scanning
- **Docker** for containerization
- **Self-hosted Runner** (e.g., `atlas`) for workflow execution
- **Argo CD** for Continuous Deployment to a Kubernetes cluster

---

## 🧪 CI/CD Workflow Overview

### 🔐 Security Check (Trivy + Gitleaks)
- Scans source code using:
  - **Trivy**: Detects vulnerabilities in the file system
  - **Gitleaks**: Detects secrets or sensitive data in the repository
- Uploads reports as GitHub Actions artifacts

### ✅ Testing
- Lints code with **flake8**
- Runs unit tests using **pytest**
- Triggered only if the security checks pass

### 🐳 Docker Image Build and Push
- Builds Docker image tagged with the short commit SHA
- Scans the Docker image using **Trivy**
- Pushes the image to **Docker Hub**

### 🚀 Kubernetes Deployment Update
- Updates the Kubernetes deployment YAML with the new Docker image tag
- Commits the change back to the `main` branch
- Argo CD monitors the updated manifest and applies the change to the cluster automatically

---

## 🛠️ Prerequisites

- Docker Hub account with:
  - `DOCKERHUB_USERNAME`
  - `DOCKERHUB_TOKEN`
  - `DOCKERHUB_IMAGE` (e.g., `username/repo`)
- GitHub repository secrets:
  - `DOCKERHUB_USERNAME`
  - `DOCKERHUB_TOKEN`
  - `DOCKERHUB_IMAGE`
- Argo CD running and synced with this repo
- Kubernetes cluster (local or cloud, e.g., kind, Minikube, EKS)

---

## 📁 Repository Structure

```
.
├── app/                        # Flask application code
├── tests/                     # Pytest test cases
├── K8s_setup/
│   └── app-deployment.yaml    # Kubernetes Deployment manifest
├── .github/
│   └── workflows/
│       └── flask-ci.yml       # GitHub Actions workflow file
├── Dockerfile                 # Docker image definition
├── requirements.txt           # Python dependencies
└── README.md
```

---

## 🔧 GitHub Actions Self-Hosted Runner

The workflow uses a self-hosted runner labeled `atlas`. Make sure you've registered and started this runner:

```bash
# On the runner host
./config.sh --url https://github.com/<username>/<repo> --token <token>
./run.sh
```

---

## 📦 Docker Image Tagging

Each Docker image is tagged using the short SHA of the commit:

```
username/repo:<short_sha>
```

The Kubernetes deployment is automatically updated with this tag and committed back to the `main` branch, triggering Argo CD to sync.

---

## 📊 Reports

Security scan results are saved as artifacts in each workflow run:

- `fs-report.json` – Trivy file system scan
- `gitleaks-report.json` – Gitleaks secrets scan
- `trivy-image-scan.txt` – Trivy Docker image scan

---

## 🚀 Deploying via Argo CD

Once the manifest is updated, Argo CD detects the change and deploys the new image to the cluster.

Make sure your Argo CD app is pointing to the `K8s_setup/app-deployment.yaml` file in this repo.

---


