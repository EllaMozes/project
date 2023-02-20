pipeline {
    agent any

    stages {
        stage('Init') {
            steps {
                echo 'Initializing..'
                echo "Running ${env.BUILD_ID} on ${env.JENKINS_URL}"
            }
        }
        stage('Test') {
            steps {
                echo 'Testing..'
                sh "ls -la"
            }
        }
        stage('clone') {
            steps {
                echo "cloning github repo"
                sh "git diff ${env.BRANCH_NAME} master"
                sh "ls -la"
            }
        }
    }
}
