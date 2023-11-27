pipeline {
    agent { label 'docker' }

    stages {
        stage('Build and Run Docker Image') {
            steps {
                script {
                    // Build the Docker image using docker-compose
                    sh 'sudo docker-compose up --build -d'
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    // Execute your tests inside the running Docker container
                    sh 'python3 tests/e2e.py'
                }
            }
        }

        stage('Install Requirements') {
            steps {
                script {
                    // Execute your tests inside the running Docker container
                    sh 'sudo pip3 install -r requirements.txt'
                }
            }
        }
    }

    post {
        always {
            // Cleanup steps, e.g., stopping and removing the Docker container
            script {
                sh 'sudo docker-compose down'
            }
        }
    }
}
