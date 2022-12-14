FROM python:3.10

RUN apt update
RUN apt-get install cron -y
RUN alias py=python

ENV PYTHONDONTWRITEBYTECODE 1

WORKDIR /Proyecto

RUN python -m venv .env

ENV PATH="/.env/bin:$PATH"

COPY . /Proyecto/
COPY requirements.txt /Proyecto/

RUN pip install -Ur requirements.txt

EXPOSE 8000

CMD service cron start && python manage.py runserver 0.0.0.0:8000