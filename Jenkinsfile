pipeline {
    agent { label 'docker' }

    stages {
        stage('Build Docker Image') {
            steps {
                script {
                    // Build the Docker image using docker-compose
                    sh 'docker-compose -f docker-compose.yaml build'
                }
            }
        }

        stage('Run Docker Container') {
            steps {
                script {
                    // Run the Docker container using docker-compose
                    sh 'docker-compose -f docker-compose.yaml up -d'
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
                sh 'docker-compose -f docker-compose.yaml down'
            }
        }
    }
}
