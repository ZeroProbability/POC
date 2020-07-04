pipeline {
  agent any
  tools { 
        maven 'Maven 3.3.9' 
        jdk 'jdk8' 
  }
  stages {
    stage('git checkout') {
      steps {
        git(url: 'https://github.com/ZeroProbability/POC.git', branch: 'master')
      }
    }
    stage('Build webflux-server-client') {
      steps {
         sh 'cd WebfluxServerClient && ./mvnw clean install'
      }
    }
  }
}
