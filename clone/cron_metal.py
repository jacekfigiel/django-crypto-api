import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'clone.settings')
django.setup()

from coin_app.models import PreciousMetalsModel
from decouple import config
from crypto import PreciousMetals
import json
import requests

def populate_metal():
    PreciousMetalsModel.objects.all().delete()
    url = config('URL_METALS')

    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)

    if response.status_code == 200:
        json_data = json.loads(response.text)
        rates = json_data["rates"]
        metals = []
        for code, rate in rates.items():
            p = PreciousMetals(code, rate)
            metals.append(p)
        for entry in metals:
            code = entry.code
            rate = 1 / entry.rate

            PreciousMetalsModel.objects.update_or_create(
                code=code, rate=rate)
    else:
        print("Request failed - metal")

if __name__ == '__main__':
    populate_metal()
