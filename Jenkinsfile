pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // Checkout the source code from the GitHub repository
                git 'https://github.com/FAhmedS/Final-MLOPs-Project-2023.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                // Build the Docker image
                script {
                    def imageName = 'Just-Image'
                    def imageVersion = 'latest'
                    def dockerFile = 'Dockerfile'

                    // Build the Docker image using the Dockerfile
                    sh "docker build -t ${imageName}:${imageVersion} -f ${dockerFile} ."
                }
            }
        }
    }
}
