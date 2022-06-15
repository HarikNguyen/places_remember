#syntax=docker/dockerfile:1
FROM python:3.8.12-slim
ENV PYTHONUNBUFFERED 1
WORKDIR /app
COPY requirements.txt requirements.txt
# configure server
RUN set -ex
RUN apt-get update -y
RUN apt-get install -y python3-tk
RUN apt-get install -y  postgresql-client
# RUN apt-get install -y libpq5
# RUN apt-get install -y .build-deps gcc python-dev musl-dev postgresql-dev
RUN pip3 install -r requirements.txt
RUN apt-get install -y binutils libproj-dev gdal-bin

COPY . .

# [Security] Limit the scope of user who run the docker image
RUN adduser --disabled-password \
      --no-create-home \
      user

USER user
