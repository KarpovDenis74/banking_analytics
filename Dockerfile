
FROM python:3.8.5
WORKDIR /code
COPY ../requirements.txt .
RUN pip3 install -r requirements.txt
COPY ../ .
RUN chmod +x start.sh

# RUN python manage.py collectstatic --noinput
# CMD gunicorn banking_analytics.wsgi:application --bind 0.0.0.0:8000
