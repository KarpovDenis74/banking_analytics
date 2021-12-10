FROM python:3.8.5
WORKDIR /code
COPY ../requirements.txt .
RUN pip3 install -r requirements.txt
COPY ../ .

# RUN python manage.py collectstatic --noinput
CMD bash start.sh
