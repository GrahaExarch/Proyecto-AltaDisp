from concurrent import futures

import grpc

# Import the generated classes
import service_pb2
import service_pb2_grpc


# Create a class to implement the gRPC service
class ServiceServicer(service_pb2_grpc.ServiceServicer):
    def Method(self, request, context):
        # Implement the service method here
        pass


def serve():
    port = '50051'
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    helloworld_pb2_grpc.add_GreeterServicer_to_server(Greeter(), server)
    server.add_insecure_port('[::]:' + port)
    server.start()
    print("Server started, listening on " + port)
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()

# https://api.openweathermap.org/data/2.5/weather?lat=-33.4377756&lon=-70.6504502&appid={API key}
# Api Key = 3321cedbf87aa17d6f6b886228f05ee8
