
pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo 'Starting CI/CD Pipeline'
                echo 'Source code is available from GitHub'
            }
        }
        stage('terraform init') {
            steps {
                dir ('terraform') {
                    bat 'terraform init'
                }
            }
        }
        stage ('terraform validate') {
            steps {
                dir ('terraform') {
                    bat 'terraform validate'
                }
            }
        }
        stage('Terraform Plan') {
    steps {
        withCredentials([
            [$class: 'AmazonWebServicesCredentialsBinding',
             credentialsId: 'AWS_cred']
        ]) {
            dir('terraform') {
                bat 'terraform plan'
            }
        }
    }
        }
        stage('Build') {
            steps {
                echo 'Building Flask Application'
                bat 'dir'
            }
        }

        stage('Docker Build') {
            steps {
                echo 'Building Docker Image'
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
