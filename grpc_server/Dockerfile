FROM python:3.10
ENV PYTHONDONTWRITEBYTECODE 1

WORKDIR /weather_server

RUN python -m venv .env
# Se Activa el .env
ENV PATH="/.env/bin:$PATH"

RUN pip install grpcio-tools
RUN pip install requests

COPY . /weather_server

CMD [ "python",  "weather_server.py" ]