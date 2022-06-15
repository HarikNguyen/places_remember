# syntax=docker/dockerfile:1
FROM python:3.8.12-slim
WORKDIR /app
COPY requirements.txt requirements.txt
# configure server
RUN set -ex
RUN apt-get update -y
RUN apt-get install -y python3-tk 
RUN pip3 install -r requirements.txt

COPY . .

RUN python3 manage.py makemigrations
RUN python3 manage.py migrate

EXPOSE 8000
CMD python3 manage.py runserver 0.0.0.0:8000