pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/vetrivel1411/sample.git'
            }
        }
        stage('Build Docker Image') {
            steps {
                script {
                    sh "docker build -t my-image ."
                }
            }
        }
}
    
    }
