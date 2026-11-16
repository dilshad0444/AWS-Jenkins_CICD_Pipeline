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
<<<<<<< HEAD
            bat 'ls -la'
        }
    }
    stage('Test') {
        steps {
            echo 'Checking application files'
            bat 'test -f app.py'
            bat 'test -f Dockerfile'
            bat 'test -f requirements.txt'
=======
            bat 'dir'
>>>>>>> eb68647ec6bdc0b9132306a91410ee9dfc28a7fc
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
