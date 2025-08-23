pipeline {
    agent any
    stages {
        stage('Check Tools') {
            steps {
                bat 'where git'
                bat 'git --version'
                bat 'echo %PATH%'
            }
        }
    }
}
