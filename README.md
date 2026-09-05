# OTUS QA Automation (Python)

Репозиторий с практическими работами и автотестами курса **Автоматизатор тестирования на Python**

## Структура проекта

* `homework/homework_01/` — **ДЗ №1**: [Устранить ошибки в скрипте с помощью линтеров](https://github.com/OtusTeam/QA-Python/blob/master/linter/hw.md).
* `homework/homework_02/` — **ДЗ №2**: [ООП на практике](https://github.com/OtusTeam/QA-Python/blob/master/oop/hw.md).
* `homework/homework_03/` — **ДЗ №3**: [Покрыть тестами код из ДЗ "ООП на практике"](https://github.com/OtusTeam/QA-Python/blob/master/pytest/hw.md).
* `homework/homework_04/` — **ДЗ №4**: [Работа с тестовыми данными](https://github.com/OtusTeam/QA-Python/blob/master/test-data/hw.md).
* `homework/homework_05/` — **ДЗ №5**: [Тестирование API](https://github.com/OtusTeam/QA-Python/blob/master/api/hw.md).
* `homework/homework_06/` + `docker-compose.yaml` — **ДЗ №6**: [Написание простых автотестов и основы Selenium](https://github.com/OtusTeam/QA-Python/blob/master/selenium/hw.md).
* `homework/homework_07/` — **ДЗ №7**: [PageObject](https://github.com/OtusTeam/QA-Python/blob/master/pageobject/hw.md).
* `homework/homework_08/` — **ДЗ №8**: [Логирование и отчетность](https://github.com/OtusTeam/QA-Python/blob/master/reporting/hw.md).
* `Dockerfile` — **ДЗ №9**: [Написать Dockerfile для своего проекта](https://github.com/OtusTeam/QA-Python/blob/master/docker/hw.md).
* `homework/homework_10/` + `browsers.json` + `docker-compose-selenoid.yaml` — **ДЗ №10**: [Написать docker-compose.yml файл для своего проекта](https://github.com/OtusTeam/QA-Python/blob/master/docker-compose/hw.md).
* `browsers.json` + `docker-compose-selenoid.yaml` — **ДЗ №11**: [Selenoid](https://github.com/OtusTeam/QA-Python/blob/master/selenoid/hw.md).

## Инфраструктура PrestaShop (http://localhost:8081/) — ДЗ №6-9

```shell
docker compose up -d
```

```shell
docker compose down -v
```

## Тесты в контейнере

```shell
docker build -t tests .
```

```shell
docker run -it tests [путь к папке ДЗ] [параметры pytest]
```

## Мониторинг контейнеров

```shell
docker ps
```

```shell
docker ps -a
```

```shell
docker images
```

```shell
docker system prune -a
```

## Инфраструктура PrestaShop с Selenoid — ДЗ №10-11

```shell
docker network create selenoid
```

```shell
docker pull selenoid/chrome:128.0
```

```shell
docker pull selenoid/firefox:125.0
```

```shell
docker compose -f docker-compose-selenoid.yaml up -d
```

```shell
docker compose -f docker-compose-selenoid.yaml up --build tests_chrome
```

```shell
docker compose -f docker-compose-selenoid.yaml up --build tests_firefox
```

```shell
docker compose -f docker-compose-selenoid.yaml down -v
```

```shell
docker system prune -a --volumes -f
```
