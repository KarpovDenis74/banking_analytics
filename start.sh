#!/bin/bash
echo "................ Запускаем WEB-сервер и CELERY(worker)........................................"
gunicorn banking_analytics.wsgi:application --bind 0.0.0.0:8000 & celery -A banking_analytics worker -l info