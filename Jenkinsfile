pipeline {
	agent any
	options {
        disableConcurrentBuilds()
        buildDiscarder logRotator(daysToKeepStr: '5', numToKeepStr: '20')
          }
	stages {
		stage('Git Checkout') {
			steps {
				script {
					properties([pipelineTriggers([pollSCM('* * * * *')])])
				}
				git 'https://github.com/udisco/project-part4.git'
			}
		}
		stage('install dependencies') {
   			steps {
      				script {
            				sh 'pip3 install Flask flask pymysql requests -t ./'
				}
			}
		}
		stage('run rest_app') {
			steps {
				script {
					sh 'nohup python3 rest_app.py &'
				}
			}
		}
		stage('Run Backend Testing') {
			steps {
				script {
					sh 'python3 backend_testing.py'
				}
			}
		}
		stage('Run Clean Environment') {
			steps {
				script {
					sh 'python3 clean_environment.py'
				}
			}
		}
        stage('Build Docker Image') {
			steps {
				script {
					sh 'docker build -t docker_rest:docker_rest .'
				}
			}
		}
		stage('Push Docker Image to Hub') {
			steps {
				script {
					sh 'docker push'
				}
			}
		}
		stage('Set Docker Compose version') {
			steps {
				script {
					sh 'echo IMAGE_TAG=${BUILD_NUMBER}>.env'
				}
			}
		}
		stage('Run Docker Compose') {
			steps {
				script {
					sh 'docker-compose up -d'
				}
			}
		}
		stage('Test Dockerized app') {
			steps {
				script {
					sh 'python3 docker_backend_testing.py'
				}
			}
		}
		stage('Run final Clean Environment') {
			steps {
				script {
					sh 'docker compose down'
				}
			}
		}
	}
}
