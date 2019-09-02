pipeline {
    agent any
    stages {
        stage('Build') { 
        
            steps {
                sh 'make install'
                script{
                    try {
                        sh 'mkdir dist'
                    } catch (err) {
                        echo 'mkdir already exists'
                    }
                }
                sh 'tar cvzf artifact.tar.gz * && mv artifact.tar.gz dist '
                archiveArtifacts artifacts:'dist/artifact.tar.gz', fingerprint: true
            }
        }
        stage("Test"){
            steps{
                sh 'pipenv run make'
            }
    }
}
}
