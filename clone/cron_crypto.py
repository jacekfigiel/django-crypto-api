import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'clone.settings')
django.setup()

from coin_app.models import CryptoModel
from decouple import config
from crypto import Crypto
import json
import requests


def populate_crypto():
    CryptoModel.objects.all().delete()
    url = config('URL_CRYPTO')
    headers = {'CMC_PRO_API_KEY': config('CMC_PRO_API_KEY')}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        json_data = json.loads(response.text)
        crypto_data = []
        for crypto in json_data['data']:
            name = crypto['name']
            symbol = crypto['symbol']
            price = crypto['quote']['USD']['price']
            percent_change_24h = crypto['quote']['USD']['percent_change_24h']
            percent_change_7d = crypto['quote']['USD']['percent_change_7d']
            market_cap = crypto['quote']['USD']['market_cap']
            volume_24h = crypto['quote']['USD']['volume_24h']
            circulating_supply = crypto['circulating_supply']
            crypto_obj = Crypto(name, symbol, price, percent_change_24h, percent_change_7d, market_cap, volume_24h, circulating_supply)
            crypto_data.append(crypto_obj)
        for entry in crypto_data:
            name = entry.name
            symbol = entry.symbol
            price = entry.price
            percent_change_24h = entry.percent_change_24h
            percent_change_7d = entry.percent_change_7d
            market_cap = entry.market_cap
            volume_24h = entry.volume_24h
            circulating_supply = entry.circulating_supply

            CryptoModel.objects.update_or_create(
                name=name, symbol=symbol, price=price, percent_change_24h=percent_change_24h,
                percent_change_7d=percent_change_7d, market_cap=market_cap, volume_24h=volume_24h,
                circulating_supply=circulating_supply)
    else:
        print("Request failed - crypto")

if __name__ == '__main__':
    populate_crypto()
