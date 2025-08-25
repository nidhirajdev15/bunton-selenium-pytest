pipeline {
    agent any
    environment {
        PATH = "C:\\Windows\\System32;C:\\Windows;${env.PATH}"
    }
    stages {
        stage('Install Dependencies') {
            steps {
                bat 'C:\\Users\\nidhi.rajdev_infobea\\AppData\\Local\\Programs\\Python\\Python313\\Scripts\\pip.exe install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                bat 'C:\\Users\\nidhi.rajdev_infobea\\AppData\\Local\\Programs\\Python\\Python313\\python.exe pytestDemo\\Test_LoginWithEmail.py --html=report.html --self-contained-html -v'
            }
        }

        stage('Publish Report') {
            steps {
                publishHTML(
                    reportDir: '.',
                    reportFiles: 'report.html',
                    reportName: 'Selenium Test Report',
                    keepAll: true,
                    alwaysLinkToLastBuild: true,
                    allowMissing: false
                )
            }
        }
    }
}