# OTUS QA Automation (Python)

Репозиторий с практическими работами и автотестами курса **Автоматизатор тестирования на Python**

## Структура проекта

* `homework/homework_01/` — **ДЗ №1**: [Устранить ошибки в скрипте с помощью линтеров](https://github.com/OtusTeam/QA-Python/blob/master/linter/hw.md).
* `homework/homework_02/` — **ДЗ №2**: [ООП на практике](https://github.com/OtusTeam/QA-Python/blob/master/oop/hw.md).
* `homework/homework_03/` — **ДЗ №3**: [Покрыть тестами код из ДЗ "ООП на практике"](https://github.com/OtusTeam/QA-Python/blob/master/pytest/hw.md).
* `homework/homework_04/` — **ДЗ №4**: [Работа с тестовыми данными](https://github.com/OtusTeam/QA-Python/blob/master/test-data/hw.md).
* `homework/homework_05/` — **ДЗ №5**: [Тестирование API](https://github.com/OtusTeam/QA-Python/blob/master/api/hw.md).
* `homework/homework_06/` — **ДЗ №6**: [Написание простых автотестов и основы Selenium](https://github.com/OtusTeam/QA-Python/blob/master/selenium/hw.md).
* `homework/homework_07/` — **ДЗ №7**: [PageObject](https://github.com/OtusTeam/QA-Python/blob/master/pageobject/hw.md).
* `homework/homework_08/` — **ДЗ №8**: [Логирование и отчетность](https://github.com/OtusTeam/QA-Python/blob/master/reporting/hw.md).
* `Dockerfile` — **ДЗ №9**: [Написать Dockerfile для своего проекта](https://github.com/OtusTeam/QA-Python/blob/master/docker/hw.md).

## Инфраструктура PrestaShop (http://localhost:8081/)

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
