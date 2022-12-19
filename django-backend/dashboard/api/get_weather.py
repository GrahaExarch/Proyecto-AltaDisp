
from django.http import JsonResponse
from rest_framework import status
from rest_framework.views import APIView
from grpc_server import weather_client, weather_pb2, weather_pb2_grpc, weather_server


class GetWeather(APIView):
    def get(self, request):
        try:
            data = weather_client.run()
            print(data)
        except Exception:
            return JsonResponse({"status": False}, status=status.HTTP_200_OK)
        return JsonResponse(
            {"status": True, "weather": data },
            status=status.HTTP_200_OK,
        )