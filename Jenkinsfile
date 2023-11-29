pipeline {
    agent { label 'docker' }

    environment {
        DOCKER_COMPOSE_FILE = 'docker-compose.yaml'
        CONTAINER_NAME = 'my_container'
        DOCKERHUB_REPO = 'damar12/wog'
    }

    stages {
        stage('Checkout') {
            steps {
                script {
                    def repoDir = 'WoG'
                    def repoExists = fileExists(repoDir)
                    def pipInstalled = sh(script: 'command -v pip', returnStatus: true) == 0

                    if (!repoExists) {
                        echo "Cloning the Git repository..."
                        sh 'git clone https://github.com/david1x/WoG.git'
                    } else {
                        echo "Repository already exists. Removing existing repository and cloning a fresh copy."
                        sh "rm -rf ${repoDir}"
                        sh 'git clone https://github.com/david1x/WoG.git'
                    }

                    // Install pip if not already installed
                    if (!pipInstalled) {
                        sh 'sudo apt-get update && sudo apt-get install -y python3-pip'
                    }

                    // Install requirements.txt on the Jenkins agent node
                    sh 'sudo pip3 install -r WoG/requirements.txt'
                }
            }
        }

        stage('Build') {
            steps {
                script {
                    dir('WoG') {
                        sh "sudo docker-compose -f docker-compose.yaml build"
                    }
                }
            }
        }

        stage('Run') {
            steps {
                script {
                    dir('WoG') {
                        sh "sudo docker-compose -f docker-compose.yaml up -d"
                    }
                }
            }
        }

        stage('Test') {
            steps {
                script {
                    sh 'sudo chmod +x WoG/tests/chromedriver'
                    sh 'sudo python3 WoG/tests/e2e.py'
                }
            }
        }

        stage('Finalize') {
            steps {
                script {
                    sh "sudo docker-compose -f WoG/$DOCKER_COMPOSE_FILE down"

                    // Push the Docker image to DockerHub
                    sh "sudo docker tag my_image $DOCKERHUB_REPO:latest"
                    sh "sudo docker push $DOCKERHUB_REPO:latest"
                
                }
            }
        }
    }
}
