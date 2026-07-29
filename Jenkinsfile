pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install') {
            steps {
                sh 'pip3 install -r requirements.txt'
            }
        }

        stage('Build Docker') {
            steps {
                sh 'docker build -t flask-demo:v1 .'
            }
        }

    }
}
