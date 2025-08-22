pipeline {
  agent any
  environment { CI = 'true' }  // lets you toggle headless in tests if you like

  stages {
    stage('Checkout') {
      steps { checkout scm }   // pulls this repo + branch automatically
    }

    stage('Install Dependencies') {
      steps {
        bat 'C:\\Users\\nidhi.rajdev_infobea\\AppData\\Local\\Programs\\Python\\Python313\\Scripts\\pip.exe install -r requirements.txt'
      }
    }

    stage('Run Tests') {
      steps {
        // adjust the path if your login test lives elsewhere
        bat 'C:\\Users\\nidhi.rajdev_infobea\\AppData\\Local\\Programs\\Python\\Python313\\python.exe pytestDemo\\Test_LoginWithEmail.py --html=report.html --self-contained-html -v'
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
