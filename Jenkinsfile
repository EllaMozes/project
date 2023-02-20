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
        stage('Test') {
            steps {
                echo "cloning github repo"
                sh "git clone https://github.com/EllaMozes/project.git"
            }
        }
    }
}

