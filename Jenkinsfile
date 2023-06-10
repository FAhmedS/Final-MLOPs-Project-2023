pipeline {
    agent any
    stages {
        stage('Main Branch Init') {
            steps {
                echo 'Initializing..'
                echo "Running ${env.BUILD_ID} on ${env.JENKINS_URL}"
                checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[credentialsId: 'MLOPs_SSH', url: 'git@github.com:FAhmedS/Final-MLOPs-Project-2023.git']])
                echo 'CHECKOUT SUCCESSFLLLLLL'
            }
        }
        stage('Test') {
            steps {
                echo 'Testing..'
                echo 'Running pytest..'
            
            }
        }
        stage('Build') {
            steps {
                echo 'Building..'
                echo 'Running docker build -t sntshk/cotu .'
                bat 'docker build -t flaskImage:latest .'
            }
        }
        stage('Publish') {
            steps {
                echo 'Publishing..'
                echo 'Running docker push..'
                bat 'docker container run -d -p 8080:80 :latest'
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
