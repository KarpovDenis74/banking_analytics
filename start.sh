#!/bin/bash
echo "................ Запускаем WEB-сервер и CELERY(worker)........................................"
python manage.py migrate
# python manage.py createcachetable
python manage.py collectstatic  --noinput
gunicorn banking_analytics.wsgi:application --bind 0.0.0.0:8000 & celery -A banking_analytics worker -l info