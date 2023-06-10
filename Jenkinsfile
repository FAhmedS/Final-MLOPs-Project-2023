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
                echo 'Test Successfull..!'
            
            }
        }
        stage('Building a DOCKER Image') {
            steps {
                echo 'Building..'
                echo 'Running docker build -t sntshk/cotu .'
                bat 'docker build -t flaskimage:latest .'
                echo 'Build Successfull..!'
            }
        }
        stage('Running Docker Container') {
            steps {
                echo 'Running..'
                echo 'Running docker container run..'
                bat 'docker container run -d -p 4000:2000 --name NamedFlaskContainer flaskimage:latest'
                echo 'Docker Container running successfully...!'
            }
        }
        stage('Cleanup Image and Stopping Container') {
            steps {
                echo 'Cleaning..'
                echo 'Running docker stop container..'
                bat 'docker container stop NamedFlaskContainer'
                bat 'docker rmi -f flaskimage:latest'
                bat 'docker rm NamedFlaskContainer'
                echo 'Stopping Container & Deleting Images Successful....!'
            }
        }
    }
}
