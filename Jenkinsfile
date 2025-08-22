pipeline {
    agent any
    environment { CI = 'true' }

    stages {
        stage('Install Dependencies') {
            steps {
                // Jenkins can now find python and pip via the corrected PATH
                bat 'pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                // Pytest is also in the PATH now
                bat 'pytest --html=report.html --self-contained-html'
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