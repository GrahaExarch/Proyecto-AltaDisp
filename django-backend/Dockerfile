FROM python:3.10

RUN apt update
RUN apt-get install cron -y
RUN alias py=python

ENV PYTHONDONTWRITEBYTECODE 1

WORKDIR /Proyecto

RUN python -m venv venv

ENV PATH="/.env/bin:$PATH"

COPY requirements.txt /Proyecto/requirements.txt

RUN pip install -Ur requirements.txt

RUN mkdir /cron
RUN touch /cron/django_cron.log

COPY . /Proyecto/

EXPOSE 8000

RUN python manage.py crontab add

CMD service cron start && python manage.py runserver 0.0.0.0:8000 

