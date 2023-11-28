pipeline {
    agent { label 'docker' }

    environment {
        DOCKER_COMPOSE_FILE = 'docker-compose.yml'
        CONTAINER_NAME = 'my_container'
    }

    stages {
        stage('Clone Git Repository') {
            steps {
                script {
                    // Clone the Git repository
                    sh 'git clone https://github.com/david1x/WoG.git'
                }
            }
        }

        stage('Check and Install pip on Node') {
            steps {
                script {
                    // Check if pip is installed
                    def pipInstalled = sh(script: 'command -v pip', returnStatus: true) == 0

                    // Install pip if not already installed
                    if (!pipInstalled) {
                        sh 'sudo apt-get update && sudo apt-get install -y python3-pip'
                    }

                    // Install requirements.txt on the Jenkins agent node
                    sh 'sudo pip3 install -r WoG/requirements.txt'
                }
            }
        }

        stage('Provide Permissions to chromedriver') {
            steps {
                script {
                    // Provide permissions to chromedriver
                    sh 'chmod +x WoG/tests/chromedriver'
                }
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    // Build the Docker image using docker-compose
                    sh "sudo docker-compose -f WoG/$DOCKER_COMPOSE_FILE build"
                }
            }
        }

        stage('Run Docker Container') {
            steps {
                script {
                    // Run the Docker container
                    sh "sudo docker-compose -f WoG/$DOCKER_COMPOSE_FILE up -d"
                }
            }
        }

        stage('Wait for Flask App to Start') {
            steps {
                script {
                    // Wait for the Flask app to respond before proceeding
                    def maxRetries = 30
                    def retryInterval = 10
                    def retries = 0

                    while (retries < maxRetries) {
                        def responseCode = sh(script: "curl -s -o /dev/null -w '%{http_code}' http://localhost:5000", returnStatus: true)

                        if (responseCode == 200) {
                            echo "Flask app is up and running!"
                            break
                        } else {
                            echo "Retrying in $retryInterval seconds..."
                            sleep(retryInterval)
                            retries++
                        }
                    }

                    if (retries == maxRetries) {
                        error "Failed to wait for Flask app to start."
                    }
                }
            }
        }

        stage('Run E2E Tests') {
            steps {
                script {
                    // Execute your E2E tests outside the Docker container
                    sh "python3 WoG/tests/e2e.py"
                }
            }
        }
    }

    post {
        always {
            // Cleanup steps, e.g., stopping and removing the Docker container
            script {
                sh "sudo docker-compose -f WoG/$DOCKER_COMPOSE_FILE down"
            }
        }
    }
}
