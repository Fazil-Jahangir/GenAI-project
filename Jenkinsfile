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
        withCredentials([string(credentialsId: 'OPENAI_API_KEY', variable: 'OPENAI_API_KEY')]) {
          sh '''
            docker run -d --restart unless-stopped \
              --name genai-app \
              -p 8000:8000 \
              -e OPENAI_API_KEY=$OPENAI_API_KEY \
              genai-app
          '''
        }
      }
    }

    stage('Smoke Test') {
      steps {
        sh 'sleep 5 && curl -f http://localhost:8000/docs > /dev/null'
      }
    }
  }
}
