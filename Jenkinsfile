pipeline {
agent any

stages {
    stage('Checkout') {
        steps {
            echo 'Starting CI/CD Pipeline'
            echo 'Source code is available from GitHub'
        }
    }
    stage('Build') {
        steps {
            echo 'Building Flask Application'
            bat 'ls'
        }
    }
    stage('Test') {
        steps {
            echo 'Checking application files'
            bat 'test -f app.py'
            bat 'test -f Dockerfile'
            bat 'test -f requirements.txt'
        }
    }
    stage('Docker Build') {
        steps {
            bat 'docker build -t devops-flask-app .'
        }
    }
}
post {
    success {
        echo 'CI/CD Pipeline completed successfully!'
    }
    failure {
        echo 'CI/CD Pipeline failed!'
    }
}

}
