pipeline {
    agent { label 'docker' }

    environment {
        DOCKER_IMAGE = 'damar12/wog:latest'
    }

    stages {
        stage('Install Requirements on Node') {
            steps {
                script {
                    // Install requirements.txt on the Jenkins agent node
                    sh 'sudo pip3 install -r requirements.txt'
                }
            }
        }

        stage('Pull Docker Image') {
            steps {
                script {
                    // Pull the Docker image from Docker Hub
                    sh "sudo docker pull $DOCKER_IMAGE"
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    // Execute your tests inside the pulled Docker image
                    sh 'python3 tests/e2e.py'
                }
            }
        }

        stage('Install Requirements in Docker Image') {
            steps {
                script {
                    // Execute your tests inside the pulled Docker image
                    sh "sudo docker run --rm $DOCKER_IMAGE pip install -r requirements.txt"
                }
            }
        }
    }

    post {
        always {
            // Cleanup steps, e.g., stopping and removing the Docker container
            script {
                sh "sudo docker-compose down"
            }
        }
    }
}
