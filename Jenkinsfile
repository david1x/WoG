pipeline {
    agent { label 'docker' }

    environment {
        DOCKER_IMAGE = 'damar12/wog:latest'
    }

    stages {
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

        stage('Install Requirements') {
            steps {
                script {
                    // Execute your tests inside the pulled Docker image
                    sh 'sudo pip3 install -r requirements.txt'
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
