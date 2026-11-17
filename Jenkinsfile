pipeline {
agent any

stages {
    stage('Checkout') {
        steps {
            echo 'Starting CI/CD Pipeline'
            echo 'Source code is available from GitHub'
        }
    }
    stage('Terraform Init') {
        steps {
            dir('terraform') {
                bat 'terraform init'
            }
        }
    }
    stage('Terraform Validate') {
        steps {
            dir('terraform') {
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
                    bat 'terraform plan -out=tfplan'
                }
            }
        }
    }
    stage('Terraform Apply') {
        steps {
            input message: 'Do you approve Terraform Apply?', ok: 'Apply'
            withCredentials([
                [$class: 'AmazonWebServicesCredentialsBinding',
                 credentialsId: 'AWS_cred']
            ]) {
                dir('terraform') {
                    bat 'terraform apply -auto-approve tfplan'
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
    stage ('Terraform destroy') {
        steps {
            bat 'terraform destroy -auto-approve'
            echo ' Infrastructure destroyed'
        }
    }
    stage('Terraform destroy') {
        steps {
            input message: 'Do you approve Destroy?', ok: 'yes'
            withCredentials([
                [$class: 'AmazonWebServicesCredentialsBinding',
                 credentialsId: 'AWS_cred']
            ]) {
                dir('terraform') {
                    bat 'terraform destroy -auto-approve tfplan'
                }
            }
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
