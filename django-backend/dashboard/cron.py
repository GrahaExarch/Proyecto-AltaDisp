import requests
from dashboard.models import Currency
from django.conf import settings


def fetch_usd_price():
    type = settings.API_URL
    type = type.replace("[type]", "usd")
    resp = requests.get(type)

    data = resp.json()['Dolares']
    for valores in data:
        value = valores['Valor']
        date = valores['Fecha']
    try:
        Currency.objects.create(type='USD', value=value, date=date)
    except Exception:
        return False


def fetch_uf_price():
    type = settings.API_URL
    type = type.replace("[type]", "uf")
    resp = requests.get(type)

    data = resp.json()['UFs']
    for valores in data:
        value = valores['Valor']
        date = valores['Fecha']
    try:
        Currency.objects.create(type='UF', value=value, date=date)
    except Exception:
        return False
