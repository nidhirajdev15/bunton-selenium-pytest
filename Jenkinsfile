pipeline {
    agent any
    stages {
        stage('Print PATH') {
            steps {
                echo "Running on: ${env.OS}"
                bat 'echo %PATH%'
            }
        }
        stage('Check Tools') {
            steps {
                bat '"C:\\Windows\\System32\\cmd.exe" /c where git'
                bat '"C:\\Windows\\System32\\cmd.exe" /c git --version'
                bat '"C:\\Windows\\System32\\cmd.exe" /c echo %PATH%'
            }
        }
    }
}
