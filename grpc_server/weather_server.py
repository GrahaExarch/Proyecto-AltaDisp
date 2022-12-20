from concurrent import futures

import grpc
import requests
import weather_pb2
import weather_pb2_grpc


class ReporterServicer(weather_pb2_grpc.ReporterServicer):
    def WeatherReport(self, request, context):
        request = requests.get(
            "https://api.openweathermap.org/data/2.5/weather?q=Santiago,cl&appid=3321cedbf87aa17d6f6b886228f05ee8&units=metric&lang=es"
        )
        weather_reply = weather_pb2.WeatherResponse()
        weather_reply.json_message = request.text
        return weather_reply


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    weather_pb2_grpc.add_ReporterServicer_to_server(ReporterServicer(), server)
    server.add_insecure_port("weather:50051")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    serve()

# https://api.openweathermap.org/data/2.5/weather?lat=-33.4377756&lon=-70.6504502&appid={APIKEY}
# Api Key = 3321cedbf87aa17d6f6b886228f05ee8
