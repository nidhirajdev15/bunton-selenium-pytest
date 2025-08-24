pipeline {
    agent any
    environment {
        PATH = "C:\\Windows\\System32;C:\\Windows;${env.PATH}"
    }
    stages {
        stage('Test') {
            steps {
                bat 'echo Hello from Jenkins'
            }
        }
    }
}