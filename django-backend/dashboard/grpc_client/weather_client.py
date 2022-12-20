import importlib

import grpc

from . import weather_pb2
from . import weather_pb2_grpc


def run():
    with grpc.insecure_channel("weather:50051") as channel:
        stub = weather_pb2_grpc.ReporterStub(channel)
        weather_request = weather_pb2.WeatherRequest()
        weather_reply = stub.WeatherReport(weather_request)
        return weather_reply


if __name__ == "__main__":
    run()
