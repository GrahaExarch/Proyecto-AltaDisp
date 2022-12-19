import weather_pb2_grpc
import weather_pb2
import grpc
import google.protobuf.json_format

def run():
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = weather_pb2_grpc.ReporterStub(channel)
        weather_request = weather_pb2.WeatherRequest()
        weather_reply = stub.WeatherReport(weather_request)
        return weather_reply

if __name__ == "__main__":
    run()