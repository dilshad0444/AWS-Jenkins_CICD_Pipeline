AWS End-to-End CI/CD Pipeline Using Jenkins, Docker and Terraform

Project Overview

This project demonstrates an end-to-end CI/CD pipeline that automates application deployment using Jenkins, Docker and AWS.

The application is developed using Python Flask and containerized using Docker. Terraform is used for AWS infrastructure provisioning.

Technologies Used

* AWS EC2
* AWS VPC
* Terraform
* Jenkins
* Docker
* Python Flask
* Git
* GitHub
* Linux

Project Architecture

Developer → GitHub → Jenkins → Docker Build → Docker Image → AWS EC2 → Application Deployment

Project Structure

CI-CD-Pipeline/
│
├── Terraform/
│   ├── main.tf
│   ├── variables.tf
│   └── output.tf
│
├── app.py
├── Dockerfile
├── Jenkinsfile
├── requirements.txt
└── README.md

Application Features

* Python Flask web application.
* Docker containerization.
* Health check endpoint.
* Automated build and deployment using Jenkins (planned).

Docker Implementation

Build Docker Image

docker build -t devops-flask-app .

Run Docker Container

docker run -d -p 5000:5000 --name devops-flask-container devops-flask-app

Check Running Containers

docker ps

Access Application

http://localhost:5000

Health Check

http://localhost:5000/health

Terraform Implementation

Terraform configuration files are maintained inside the Terraform directory.

Initialize Terraform:

terraform init

Validate configuration:

terraform validate

Generate execution plan:

terraform plan

CI/CD Pipeline

The planned Jenkins pipeline consists of:

1. Source code checkout from GitHub.
2. Application build.
3. Application testing.
4. Docker image creation.
5. Docker image push to registry.
6. Automated deployment to AWS.

Project Goals

* Understand CI/CD automation.
* Automate infrastructure provisioning.
* Learn Docker containerization.
* Integrate Jenkins with GitHub.
* Deploy applications on AWS.

Author

AWS & DevOps Learner