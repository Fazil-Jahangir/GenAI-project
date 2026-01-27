pipeline {
  agent any

  environment {
    IMAGE_NAME = "genai-resume-api"
    CONTAINER_NAME = "genai-resume-api"
    APP_PORT = "8000"
    OLLAMA_HOST = "http://host.docker.internal:11434"
  }

  stages {
    stage("Checkout") {
      steps { checkout scm }
    }

    stage("Build") {
      steps {
        sh """
          docker build -t ${IMAGE_NAME}:latest .
        """
      }
    }

    stage("Deploy") {
      steps {
        sh """
          docker rm -f ${CONTAINER_NAME} || true

          docker run -d --restart unless-stopped \\
            --name ${CONTAINER_NAME} \\
            -p ${APP_PORT}:8000 \\
            --add-host=host.docker.internal:host-gateway \\
            -e OLLAMA_HOST=${OLLAMA_HOST} \\
            ${IMAGE_NAME}:latest

          docker ps | grep ${CONTAINER_NAME}
        """
      }
    }
  }
}
