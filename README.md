# [***«Проект «Финансовая аналитика»»***](http://github.com/KarpovDenis74/banking_analytics)

[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)

#### [Проект размещен на сайте]

----
    Сайт аналитики активов финансовых организаций удобно навигированный и структурированный.
    Пользователь может получить аналитику в разрезе периодов, разделов, статей учета 
    финансовых показателей кредитных организаций. Можно посмотреть новости в разезе организаций,
    а также как менялись показатели в период выхода новостей. 
    Можно выбрать отдельную организацию и выбрать исследуемые разделы баланса 
    или отдельные статьи раздела. Также можно выбрать анализируемые показатели по выбранным 
    организациям. 
    Можно подписаться на выход новых данных по организации.
----

## [Подготовка к работе]


1 Скопируйте в рабочую диреторию:
    ```
        DockerFile
        docker-compose.yaml
    ```
2 Создайте файл .env и заполните его своими значениями. 
    Все нужные переменные и их примерные значения описаны файле 
        ```
            .env.template
        ```
3 Запустите процесс сборки и запуска контейнеров:  
    ```
        docker-compose up
    ```
4 Примените миграции, введите:  
    ```
        docker-compose -f docker-compose.yaml exec web python manage.py migrate --noinput
    ```
5 Создайте суперпользователя, необходимо ввести:  
    ```
        docker-compose -f docker-compose.yaml exec web python manage.py createsuperuser
    ```
6 Добавьте  в базу ghbмеры банков и курсы валют (данные будут взяты из папки data_csv):  
    ```
        docker-compose -f docker-compose.yaml exec web python manage.py load_banks
        docker-compose -f docker-compose.yaml exec web python manage.py load_currency
    ```
7 Собирите статику:  
    ```
        docker-compose -f docker-compose.yaml exec web python manage.py collectstatic --noinput
    ```
Вы великолепны !!! 
   
## [Технологии]
-------------
* [Python](https://www.python.org/) - высокоуровневый язык программирования общего назначения;
* [Django](https://www.djangoproject.com/) - фреймворк для веб-приложений;
* [Django REST framework](https://www.django-rest-framework.org/) - API фреймворк для Django;
* [PostgreSQL](https://www.postgresql.org/) - объектно-реляционная система управления базами данных;
* [Nginx](https://nginx.org/) - HTTP-сервер и обратный прокси-сервер, почтовый прокси-сервер, а также TCP/UDP прокси-сервер общего назначения;
* [Docker](https://www.docker.com/) - ПО для автоматизации развёртывания и управления приложениями в средах с поддержкой контейнеризации;
* [Docker-Compose](https://docs.docker.com/compose/) - инструмент для создания и запуска многоконтейнерных Docker приложений. 
