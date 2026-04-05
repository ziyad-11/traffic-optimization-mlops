pipeline {
    agent any

    stages {

       stage('Clone Repository') {
    steps {
        git branch: 'main', url: 'https://github.com/ziyad-11/traffic-optimization-mlops.git'
    }
}

       stage('Install Dependencies') {
    steps {
        bat '"C:\\Users\\ziyad mulla\\AppData\\Local\\Python\\bin\\python.exe" -m pip install -r requirements.txt'
    }
}

        stage('Train Model') {
    steps {
        bat '"C:\\Users\\ziyad mulla\\AppData\\Local\\Python\\bin\\python.exe" src/train_model.py'
    }
}

        stage('Build Docker Image') {
            steps {
                bat 'docker build -t traffic-mlops .'
            }
        }

        stage('Run Container') {
            steps {
                bat 'docker run -p 8000:8000 traffic-mlops'
            }
        }
    }
}