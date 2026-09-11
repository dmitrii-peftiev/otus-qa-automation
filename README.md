# OTUS QA Automation (Python)

Репозиторий с практическими работами и автотестами курса **Автоматизатор тестирования на Python**

## Структура проекта

| ДЗ № | Путь к директории / файлу                                                                                                                                                          | Техническое задание                                                                                                           |
|:----:|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------------------------------------------------|
|  1   | **[`homework/homework_01/`](./homework/homework_01/)**                                                                                                                             | [Устранить ошибки в скрипте с помощью линтеров](https://github.com/OtusTeam/QA-Python/blob/master/linter/hw.md)               |
|  2   | **[`homework/homework_02/`](./homework/homework_02/)**                                                                                                                             | [ООП на практике](https://github.com/OtusTeam/QA-Python/blob/master/oop/hw.md)                                                |
|  3   | **[`homework/homework_03/`](./homework/homework_03/)**                                                                                                                             | [Покрыть тестами код из ДЗ "ООП на практике"](https://github.com/OtusTeam/QA-Python/blob/master/pytest/hw.md)                 |
|  4   | **[`homework/homework_04/`](./homework/homework_04/)**                                                                                                                             | [Работа с тестовыми данными](https://github.com/OtusTeam/QA-Python/blob/master/test-data/hw.md)                               |
|  5   | **[`homework/homework_05/`](./homework/homework_05/)**                                                                                                                             | [Тестирование API](https://github.com/OtusTeam/QA-Python/blob/master/api/hw.md)                                               |
|  6   | **[`homework/homework_06/`](./homework/homework_06/)**<br>[`docker-compose.yaml`](./docker-compose.yaml)                                                                           | [Написание простых автотестов и основы Selenium](https://github.com/OtusTeam/QA-Python/blob/master/selenium/hw.md)            |
|  7   | **[`homework/homework_07/`](./homework/homework_07/)**                                                                                                                             | [PageObject](https://github.com/OtusTeam/QA-Python/blob/master/pageobject/hw.md)                                              |
|  8   | **[`homework/homework_08/`](./homework/homework_08/)**                                                                                                                             | [Логирование и отчетность](https://github.com/OtusTeam/QA-Python/blob/master/reporting/hw.md)                                 |
|  9   | **[`Dockerfile`](./Dockerfile)**                                                                                                                                                   | [Написать Dockerfile для своего проекта](https://github.com/OtusTeam/QA-Python/blob/master/docker/hw.md)                      |
|  10  | **[`homework/homework_10/`](./homework/homework_10/)**<br>[`browsers.json`](./browsers.json)<br>[`docker-compose-selenoid.yaml`](./docker-compose-selenoid.yaml)                   | [Написать docker-compose.yml файл для своего проекта](https://github.com/OtusTeam/QA-Python/blob/master/docker-compose/hw.md) |
|  11  | **[`quota/test.xml`](./quota/test.xml)**<br>[`browsers.json`](./browsers.json)<br>[`docker-compose-selenoid.yaml`](./docker-compose-selenoid.yaml)<br>[`nginx.conf`](./nginx.conf) | [Selenoid](https://github.com/OtusTeam/QA-Python/blob/master/selenoid/hw.md)                                                  |
|  12  | **[`Jenkinsfile`](./Jenkinsfile)**                                                                                                                                                 | [Запуск автотестов с использованием Jenkins](https://github.com/OtusTeam/QA-Python/blob/master/jenkins/hw.md)                 |

## Инструкции по развертыванию и запуску

<details>
<summary><b>Инфраструктура PrestaShop (ДЗ №6-9)</b></summary>

### Развертывание локального стенда

```bash
docker compose up -d
```

```bash
docker compose down -v
```

### Запуск автотестов в контейнере

```bash
docker build -t tests .
```

```bash
docker run -it tests [путь к папке ДЗ] [параметры pytest]
```

### Мониторинг и очистка Docker-ресурсов

```bash
docker ps
```

```bash
docker ps -a
```

```bash
docker images
```

```bash
docker system prune -a
```

</details>

<details>
<summary><b>Инфраструктура PrestaShop с Selenoid (ДЗ №10-11)</b></summary>

### Подготовка инфраструктуры Selenoid

```bash
docker network create selenoid
```

```bash
docker pull selenoid/chrome:128.0
```

```bash
docker pull selenoid/firefox:125.0
```

```bash
docker compose -f docker-compose-selenoid.yaml up -d
```

### Запуск тестов в контейнерах браузеров

```bash
docker compose -f docker-compose-selenoid.yaml up --build tests_chrome
```

```bash
docker compose -f docker-compose-selenoid.yaml up --build tests_firefox
```

### Очистка ресурсов

```bash
docker compose -f docker-compose-selenoid.yaml down -v
```

```bash
docker system prune -a --volumes -f
```

</details>


<details>
<summary><b>Запуск автотестов через Jenkins (ДЗ №12)</b></summary>

### Подготовка инфраструктуры

```bash
docker run -d --name jenkins -p 8088:8080 -p 50000:50000 --restart=on-failure -v jenkins_home:/var/jenkins_home -v /var/run/docker.sock:/var/run/docker.sock --user root jenkins/jenkins:lts
```

```bash
docker exec -u root jenkins sh -c "apt-get update && apt-get install -y docker.io && apt-get clean"
```

```bash
docker network connect selenoid jenkins
```

### Первоначальная настройка (http://localhost:8088)

```bash
docker exec jenkins cat /var/jenkins_home/secrets/initialAdminPassword
```

* Установить `Allure Jenkins plugin`.
* В Tools добавить Allure с именем: `allure`.

### Очистка Jenkins

```bash
docker stop jenkins
```

```bash
docker rm -f jenkins
```

```bash
docker volume rm jenkins_home
```

</details>