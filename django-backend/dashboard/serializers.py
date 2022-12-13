from dashboard.models import Currency
from rest_framework.serializers import ModelSerializer


class CurrencySerializer(ModelSerializer):
    class Meta:
        model = Currency
        fields = '__all__'
