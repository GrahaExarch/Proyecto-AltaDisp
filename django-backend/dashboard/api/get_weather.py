import json

from django.http import JsonResponse
from rest_framework import status
from rest_framework.views import APIView

from ..grpc_client import weather_client


class GetWeather(APIView):
    def get(self, request):
        try:
            data = weather_client.run()
            json_object = json.loads(data.json_message)
        except Exception:
            return JsonResponse({"status": False}, status=status.HTTP_200_OK)
        return JsonResponse(
            {"status": True, "weather": json_object},
            status=status.HTTP_200_OK,
        )
