pipeline {
    agent any

    parameters {
        string(name: 'EXECUTOR', defaultValue: 'router', description: 'Selenoid executor address')
        string(name: 'BASE_URL', defaultValue: 'http://prestashop', description: 'PrestaShop application URL')
        choice(name: 'BROWSER', choices: ['chrome', 'firefox'], description: 'Target browser')
        choice(name: 'BROWSER_VERSION', choices: ['128.0', '125.0'], description: 'Browser version')
        string(name: 'THREADS', defaultValue: '2', description: 'Number of execution threads')
    }

    stages {
        stage('Build Test Image') {
            steps {
                sh "docker build -t prestashop-tests ."
            }
        }

        stage('Run Tests') {
            steps {
                sh """
                    docker run --name test-run-container \
                    --network selenoid \
                    prestashop-tests \
                    homework/homework_10/tests/ \
                    -m homework_10 \
                    --executor=${params.EXECUTOR} \
                    --base-url=${params.BASE_URL} \
                    --browser=${params.BROWSER} \
                    --browser_version=${params.BROWSER_VERSION} \
                    --alluredir=allure-results
                """
            }
            post {
                always {
                    sh "docker cp test-run-container:/app/allure-results ${WORKSPACE}/allure-results || true"
                    sh "docker rm -f test-run-container || true"
                }
            }
        }
    }

    post {
        always {
            allure includeProperties: false, jdk: '', results: [[path: 'allure-results']]
        }
    }
}
