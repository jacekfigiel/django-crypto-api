FROM python:3.9-slim-buster

RUN apt update
RUN apt-get install cron -y
RUN alias py=python

WORKDIR /app

COPY . /app
COPY ./requirements.txt /app

RUN pip install -r requirements.txt

EXPOSE 8000

CMD python manage.py runserver 0.0.0.0:8000
