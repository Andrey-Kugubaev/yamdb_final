## CI (Continuous Integration) и CD (Continuous Deployment) проекта api_yamdb

https://github.com/Andrey-Kugubaev/yamdb_final/actions/workflows/yamdb_workflow.yml/badge.svg

#### Проект для реализации:
- _автоматических запуск тестов;_
- _обновлений образов на Docker Hub;_
- _автоматического деплоя на боевой сервер при пуше в главную ветку main._

Тестирование, проверка и сбор образов для **Docker** с помощью **GitHub Actions** и размещение на сервере в **Яндекс Облаке**
Об успешном прохождении тестов и демлоя на сервер приходит оповещение в телеграм-бот.

### Инструкция по запуску:
- Склонируйте проект
`git clone https://github.com/Andrey-Kugubaev/yamdb_final.git`
- перейдите в директорию _yamdb_final_
`cd yamdb_final`
- запустите _docker-compose_
`docker-compose up`
- выполните миграции
`docker-compose exec web python manage.py migrate`
- создайте суперпользователя
`docker-compose exec web python manage.py createsuperuser`
- заполните базу тестовыми данными
`docker-compose exec web python manage.py loaddata fixtures.json`

#### Документация по использованию: _http://localhost/redoc/_

_Проект когда-то был доступен по адресу:
http://84.252.137.87/redoc/_