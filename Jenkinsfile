pipeline {

    agent any

    stages {

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t flask-demo .'
            }
        }

        stage('Stop Old Container') {
            steps {
                sh '''
                docker rm -f flask-demo || true
                '''
            }
        }

        stage('Run Container') {
            steps {
                sh '''
                docker run -d \
                --name flask-demo \
                -p 5001:5000 \
                flask-demo
                '''
            }
        }

        stage('Verify') {
            steps {
                sh 'docker ps'
            }
        }

    }
}

