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
|  13  | **[`homework/homework_13/`](./homework/homework_13/)**                                                                                                                             | [Автоматизация жестов и поиск элементов в Appium](https://github.com/OtusTeam/QA-Python/blob/master/mobile/hw.md)             |
|  14  | **[`homework/homework_14/`](./homework/homework_14/)**                                                                                                                             | [Работа с ОС Linux с помощью Python](https://github.com/OtusTeam/QA-Python/blob/master/linux/hw.md)                           |
|  15  | **[`homework/homework_15/`](./homework/homework_15/)**                                                                                                                             | [Анализ лога веб-сервера](https://github.com/OtusTeam/QA-Python/blob/master/log/hw.md)                                        |
|  16  | **[`homework/homework_16/`](./homework/homework_16/)**                                                                                                                             | [Echo сервер](https://github.com/OtusTeam/QA-Python/blob/master/socket/hw.md)                                                 |

## Инструкции по развертыванию и запуску

<details>
<summary><strong>Инфраструктура PrestaShop <code>ДЗ №6-9</code></strong></summary>

### Развертывание локального стенда (http://localhost:8081)

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

---
</details>

<details>
<summary><strong>Инфраструктура PrestaShop с Selenoid <code>ДЗ №10-11</code></strong></summary>

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

---
</details>


<details>
<summary><strong>Запуск автотестов через Jenkins <code>ДЗ №12</code></strong></summary>

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

---
</details>


<details>
<summary><strong>Автоматизация жестов и поиск элементов в Appium <code>ДЗ №13</code></strong></summary>

### Подготовка инфраструктуры

* Установить `Node.js`.
* Распаковать `Android SDK Platform-Tools` в `C:\android-sdk\platform-tools`.
* Добавить в переменные среды пользователя:
    * `ANDROID_HOME` = `C:\android-sdk`
    * В `Path` добавить `C:\android-sdk\platform-tools`

* Установить `Appium` и драйвер:

```bash
npm install -g appium
```

```bash
appium driver install uiautomator2
```

* Подключить устройство на `Android` и включить отладку по USB.

### Запуск автотестов

```bash
appium
```

```bash
pytest homework/homework_13/tests/ -m homework_13
```

---
</details>

<details>
<summary><strong>Парсер процессов Linux <code>ДЗ №14</code></strong></summary>

### Подготовка инфраструктуры

```bash
docker run -it -v "${PWD}:/app" -w /app/homework/homework_14 --name process-checker ubuntu:latest
```

```bash
apt-get update
```

```bash
apt-get install -y procps python3
```

### Запуск парсера процессов

```bash
python3 process_parser.py
```

### Очистка ресурсов

```bash
exit
```

```bash
docker rm process-checker
```

---
</details>

<details>
<summary><strong>Анализ лога веб-сервера <code>ДЗ №15</code></strong></summary>

### Подготовка инфраструктуры

```bash
docker run -it -v "${PWD}:/app" -w /app/homework/homework_15 --name log-analyzer ubuntu:latest
```

```bash
apt-get update
```

```bash
apt-get install -y python3 python3-pip
```

### Запуск парсера логов

```bash
python3 log_parser.py --path access.log
```

### Очистка ресурсов

```bash
exit
```

```bash
docker rm log-analyzer
```

---
</details>

<details>
<summary><strong>Echo сервер <code>ДЗ №16</code></strong></summary>

### Запуск сервера

```bash
python homework/homework_16/echo_server.py
```

### Запуск автотестов

```bash
pytest homework/homework_16/tests/test_echo_server.py
```

</details>
