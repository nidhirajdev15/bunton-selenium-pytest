pipeline {
    agent any
    environment { CI = 'true' }

    stages {
        stage('Checkout') {
            steps { checkout scm }
        }

        stage('Install Dependencies') {
            steps {
                bat """
                C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe -Command "& 'C:\\Users\\nidhi.rajdev_infobea\\AppData\\Local\\Programs\\Python\\Python313\\python.exe' -m pip install -r requirements.txt"
                """
            }
        }

        stage('Run Tests') {
            steps {
                bat """
                C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe -Command "& 'C:\\Users\\nidhi.rajdev_infobea\\AppData\\Local\\Programs\\Python\\Python313\\python.exe' -m pytest --html=report.html --self-contained-html"
                """
            }
        }

        stage('Publish Report') {
            steps {
                publishHTML([
                    reportDir: '.',
                    reportFiles: 'report.html',
                    reportName: 'Selenium Test Report',
                    keepAll: true,
                    alwaysLinkToLastBuild: true,
                    allowMissing: false
                ])
            }
        }
    }
}
