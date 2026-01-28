pipeline {
    agent any

    stages {

        stage('Clone Repo') {
            steps {
                git branch: 'master',
                    url: 'https://github.com/Fazil-Jahangir/GenAI-project.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t genai-app .'
            }
        }

        stage('Stop Old Container') {
            steps {
                sh 'docker rm -f genai-container || true'
            }
        }

        stage('Run Container') {
            steps {
                sh '''
                docker run -d \
                --name genai-container \
                --env-file .env \
                -p 8000:8000 \
                genai-app
                '''
            }
        }
    }
}
