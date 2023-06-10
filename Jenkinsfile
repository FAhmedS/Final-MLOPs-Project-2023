pipeline {
    agent any

    stages {
        stage('Main Branch Init') {
            steps {
                echo 'Initializing..'
                echo "Running ${env.BUILD_ID} on ${env.JENKINS_URL}"            }
        }
        stage('Test') {
            steps {
                echo 'Testing..'
                echo 'Running pytest..'
            }
        }
        stage('Build Docker image') {
            steps {
                echo 'Building..'
                echo 'Running docker build -t sntshk/cotu .'
                sh 'docker build -t mlops-docker-image-final .'
            }
        }
        stage('Publish') {
            steps {
                echo 'Publishing..'
                echo 'Running docker push..'
            }
        }
        stage('Cleanup') {
            steps {
                echo 'Cleaning..'
                echo 'Running docker rmi..'
            }
        }
    }
}
