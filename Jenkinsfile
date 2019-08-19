pipeline {
    agent {
                docker {
                    image 'circleci/python' 
                    args '--user 0:0'
                }
            }
    stages {

        stage('Preparation') { 
            
            steps {
                    // git 'https://github.com/manrodri/stocks_price_tracking_app.git' 
                    // insert your project repo url here
                    sh 'pip3 install pipenv'
            }
        }

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
