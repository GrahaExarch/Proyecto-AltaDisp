from dashboard.models import Currency
from dashboard.serializers import CurrencySerializer
from django.http import JsonResponse
from rest_framework import status
from rest_framework.views import APIView


class GetCurrencyUSD(APIView):
    def get(self, request):
        try:
            data = Currency.objects.filter(type='USD').order_by('-date')
        except Exception:
            return JsonResponse({"status": False}, status=status.HTTP_200_OK)
        return JsonResponse(
            {"status": True, "currency": CurrencySerializer(data, many=True).data},
            status=status.HTTP_200_OK,
        )


class GetCurrencyUF(APIView):
    def get(self, request):
        try:
            data = Currency.objects.filter(type='UF').order_by('-date')
        except Exception:
            return JsonResponse({"status": False}, status=status.HTTP_200_OK)
        return JsonResponse(
            {"status": True, "currency": CurrencySerializer(data, many=True).data},
            status=status.HTTP_200_OK,
        )
