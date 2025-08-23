pipeline {
    agent any

    stages {
        stage('Diagnostics') {
            steps {
                echo "--- Starting Diagnostics ---"
                echo "Verifying environment..."
                bat 'echo %PATH%'
                echo "Verifying git version..."
                bat 'git --version'
                echo "--- Diagnostics Complete ---"
            }
        }
        stage('Manual Checkout') {
            steps {
                script {
                    try {
                        echo "Attempting to checkout SCM..."
                        // This command checks out the repository configured in the job UI
                        checkout scm
                        echo "SCM checkout successful!"
                    } catch (Exception e) {
                        echo "ERROR: SCM checkout FAILED!"
                        // This will print the detailed Java exception to the log
                        echo "Caught exception: ${e}"
                        // This is the most important line, it prints the real error message
                        echo "Full error details: ${e.getMessage()}"
                        // This will cause the build to fail, but with our custom message
                        error("Aborting build due to checkout failure. See log for details.")
                    }
                }
            }
        }
        stage('Build') {
            steps {
                // This stage will only run if the checkout succeeds
                echo 'This is where your build steps would normally run.'
            }
        }
    }
}