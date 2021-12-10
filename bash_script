#!/bin/bash
echo "................ Запускаем сервер .............................................................."
python manage.py runserver & celery -A banking_analytics worker -l info
