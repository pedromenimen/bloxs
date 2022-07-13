FROM python:3.10

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt .

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

WORKDIR /code

COPY .  /code/