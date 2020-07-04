pipeline {
  agent any
  stages {
    stage('git checkout') {
      steps {
        git(url: 'https://github.com/ZeroProbability/POC.git', branch: 'master')
      }
    stage('Build') {
         steps {
            echo 'This is a minimal pipeline.'
         }
      }
    }
  }
}
