pipeline {
  agent any

  stages {
    stage('Build Docker Image') {
      steps {
        sh 'docker build -t genai-app .'
      }
    }

    stage('Stop Old Container') {
      steps {
        sh 'docker rm -f genai-app || true'
      }
    }

    stage('Run Container') {
      steps {
        sh 'docker run -d --name genai-app -p 8000:8000 genai-app'
      }
    }
  }
}
