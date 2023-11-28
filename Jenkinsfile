pipeline {
    agent { label 'docker' }

    environment {
        DOCKER_IMAGE = 'damar12/wog:latest'
    }

    stages {
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
                    sh 'sudo pip3 install -r requirements.txt'
                }
            }
        }

        stage('Provide Permissions to chromedriver') {
            steps {
                script {
                    // Provide permissions to chromedriver
                    sh 'chmod +x tests/chromedriver'
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

        stage('Run Docker Container') {
            steps {
                script {
                    // Run the Docker container
                    sh "sudo docker run --rm -d --name my_container $DOCKER_IMAGE"
                }
            }
        }

        stage('Run E2E Tests') {
            steps {
                script {
                    // Execute your E2E tests inside the running Docker container
                    sh "python3 tests/e2e.py"
                }
            }
        }
    }

    post {
        always {
            // Cleanup steps, e.g., stopping and removing the Docker container
            script {
                sh "sudo docker stop my_container && sudo docker rm my_container"
            }
        }
    }
}
