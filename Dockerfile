FROM python:3.7

ENV PYTHONUNBUFFERED 1

RUN mkdir /drf_test

WORKDIR /drf_test
COPY requirements.txt /drf_test/

RUN python -m venv .env

RUN . /.env/bin/activate && pip install -r requirements.txt

ADD . /drf_test/