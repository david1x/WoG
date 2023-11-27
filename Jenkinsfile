pipeline {
    agent { label 'docker' }

    stages {
        stage('Build and Run Docker Image') {
            steps {
                script {
                    // Build the Docker image using docker-compose
                    sh 'docker-compose up --build -d'
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    // Execute your tests inside the running Docker container
                    sh 'python tests/e2e.py'
                }
            }
        }
    }

    post {
        always {
            // Cleanup steps, e.g., stopping and removing the Docker container
            script {
                sh 'docker-compose down'
            }
        }
    }
}
