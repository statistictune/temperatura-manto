# syntax=docker/dockerfile:1

FROM python:3.6-slim-buster

WORKDIR /app

COPY requirements.txt requirements.txt

RUN apt-get -y update

RUN apt-get install -y ffmpeg

RUN pip3 install -r requirements.txt

COPY . .

ENTRYPOINT [ "python3", "app.py"] 