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
            sh 'ls -la'
        }
    }
    stage('Test') {
        steps {
            echo 'Checking application files'
            sh 'test -f app.py'
            sh 'test -f Dockerfile'
            sh 'test -f requirements.txt'
        }
    }
    stage('Docker Build') {
        steps {
            sh 'Docker build -t devops-flask-app .'
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