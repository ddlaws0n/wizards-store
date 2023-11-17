# Wizard's Store - Flask Web Application

## Overview
Wizard's Store is a simple Flask web application designed for educational purposes. It demonstrates the development, containerization, and deployment of a Python web application using Flask, Docker, Kubernetes, and AWS.

## Features
- Flask web server serving a basic web application.
- Integration with AWS S3 for storing user registration data.
- Containerization using Docker.
- Deployment on AWS using Kubernetes (EKS).

## Prerequisites
- Python 3.8+
- Docker
- Kubernetes (kubectl)
- AWS CLI
- Podman (optional, for container development)

## Local Setup
1. **Clone the Repository**:
   ```
   git clone https://github.com/yourgithubusername/wizards-store.git
   cd wizards-store
   ```

2. **Create a Virtual Environment** (optional):
   ```
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install Dependencies**:
   ```
   pip install -r requirements.txt
   ```

4. **Run the Application Locally**:
   ```
   python run.py
   ```

## Containerization with Docker
1. **Build the Docker Image**:
   ```
   docker build -t wizards-store .
   ```

2. **Run the Container Locally**:
   ```
   docker run -p 5000:5000 wizards-store
   ```

## Deployment on AWS EKS
1. **Set up an EKS Cluster on AWS** (refer to AWS documentation).

2. **Deploy the Application to EKS**:
   - Create a Kubernetes deployment using `kubectl apply -f deployment.yaml`.
   - Expose the application with a LoadBalancer service using `kubectl apply -f service.yaml`.

## Contributing
Contributions to the project are welcome! Please fork the repository and submit a pull request with your changes.

## License
This project is open source and available under the [MIT License](LICENSE).