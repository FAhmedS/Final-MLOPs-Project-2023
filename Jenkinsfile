pipeline {
    agent {
        dockerfile true
    }

    stages {
        stage('Checkout') {
            steps {
                //Checkout
                echo 'hello world'
            }
        }

        stage('Build Docker Image') {
            steps {
                // Build the Docker image
                sh 'docker build -t image1/image1'
                }
            }
        }
    }
}
