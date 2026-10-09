# smartcampus-devops
End-to-end CI/CD project using Jenkins, GitHub Webhooks, Docker, Docker Hub and Kubernetes

# SmartCampus - DevOps CI/CD Project

An end-to-end DevOps project demonstrating automated
application delivery using GitHub, Jenkins, Docker,
Docker Hub, and Kubernetes.

## Application Features

- Student directory
- Flask REST API
- Application health endpoint
- Automated application tests
- Containerized application

## Technology Stack

- Python and Flask
- Pytest
- Docker
- Docker Hub
- Jenkins Pipeline
- GitHub Webhooks
- Kubernetes
- Linux

## CI/CD Workflow

1. Developer pushes code to GitHub.
2. GitHub webhook triggers Jenkins.
3. Jenkins checks out the repository.
4. Automated tests run.
5. Docker image is built and scanned.
6. Image is pushed to Docker Hub.
7. Kubernetes deploys the new image.
8. Health checks verify the deployment.

## Repository Structure

- app.py - Flask application and API
- requirements.txt - Python dependencies
- Dockerfile - Container image instructions
- Jenkinsfile - CI/CD pipeline
- tests/ - Automated tests
- templates/ - Web frontend
- k8s/ - Kubernetes manifests

## Security

Credentials must be stored in Jenkins Credentials.
Never commit passwords, private keys, tokens, or
kubeconfig files to GitHub.

## Project Status

Application and deployment configuration are being
prepared. Infrastructure setup and end-to-end
verification will be completed in subsequent phases.
