pipeline {

    agent {
        label 'myslave'
    }

    environment {
        DOCKERHUB_CREDENTIALS = credentials('dockerhub-creds')
    }

    stages {

        stage('Workspace Verification') {
            steps {

                sh 'echo "Current Workspace:"'
                sh 'pwd'

                sh 'echo "Project Files:"'
                sh 'ls -l'
                
            }
        }

        stage('Cleanup Old Containers and Images') {
            steps {

                sh '''
                docker rm -f auth-container product-container order-container || true
                '''

                sh '''
                docker rmi -f auth-service:v1 product-service:v1 order-service:v1 || true
                '''

                sh '''
                docker rmi -f awsarchitect2030/auth-service:v1 || true
                docker rmi -f awsarchitect2030/product-service:v1 || true
                docker rmi -f awsarchitect2030/order-service:v1 || true
                '''
            }
        }

        stage('Build Auth Service Image') {
            steps {

                sh '''
                docker build -t auth-service:v1 ./auth-service
                '''
            }
        }

        stage('Build Product Service Image') {
            steps {

                sh '''
                docker build -t product-service:v1 ./product-service
                '''
            }
        }

        stage('Build Order Service Image') {
            steps {

                sh '''
                docker build -t order-service:v1 ./order-service
                '''
            }
        }

        stage('Docker Hub Login') {
            steps {

                sh '''
                echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin
                '''
            }
        }

        stage('Tag Docker Images') {
            steps {

                sh '''
                docker tag auth-service:v1 awsarchitect2030/auth-service:v1
                '''

                sh '''
                docker tag product-service:v1 awsarchitect2030/product-service:v1
                '''

                sh '''
                docker tag order-service:v1 awsarchitect2030/order-service:v1
                '''
            }
        }

        stage('Push Images to Docker Hub') {
            steps {

                sh '''
                docker push awsarchitect2030/auth-service:v1
                '''

                sh '''
                docker push awsarchitect2030/product-service:v1
                '''

                sh '''
                docker push awsarchitect2030/order-service:v1
                '''
            }
        }

        stage('Deploy to EKS') {
            steps {

                sh '''
                kubectl apply -f k8s/
                '''

                sh '''
                kubectl get deployments
                '''

                sh '''
                kubectl get pods
                '''
            }
        }

        stage('Verify Docker Images') {
            steps {

                sh '''
                docker images
                '''
            }
        }
    }
}
