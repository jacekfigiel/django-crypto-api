import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'clone.settings')

django.setup()

from crypto import Crypto
from coin_app.models import CryptoModel
import json


def parse():
    file = open('test_data.json')
    data = json.load(file)
    result = []
    for i in data['data']:
        c = Crypto(i['name'], i['symbol'], i['quote']["USD"]["price"],
                   i['quote']["USD"]["percent_change_24h"],
                   i['quote']["USD"]["percent_change_7d"],
                   i['quote']["USD"]["market_cap"],
                   i['quote']["USD"]["volume_24h"], i["circulating_supply"])
        result.append(c)
    return result


def populate():
    for entry in parse():
        name = entry.name
        symbol = entry.symbol
        price = entry.price
        percent_change_24h = entry.percent_change_24h
        percent_change_7d = entry.percent_change_7d
        market_cap = entry.market_cap
        volume_24h = entry.volume_24h
        circulating_supply = entry.circulating_supply

        crypto_created = CryptoModel.objects.get_or_create(
            name=name, symbol=symbol, price=price, percent_change_24h=percent_change_24h,
            percent_change_7d=percent_change_7d, market_cap=market_cap,
            volume_24h=volume_24h, circulating_supply=circulating_supply)


if __name__ == '__main__':
    print("populating script!")
    populate()
    print("populating complete!!")
