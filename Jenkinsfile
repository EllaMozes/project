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
                echo 'Testing.'
                sh "ls -la"
            }
        }
        stage('diff') {
            steps {
                echo "cloning github repo"
                sh "git diff --no-index EllaMozes/${env.BRANCH_NAME} EllaMozes/master"
            }
        }
    }
}
