import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'clone.settings')

django.setup()

from crypto import Crypto, PreciousMetals
from coin_app.models import CryptoModel, PreciousMetalsModel
import json
import re
from django.core.management import call_command


def parse_crypto():
    directory = "C:/Users/agafi/IdeaProjects/coinmarketcap_clone/clone/json_files"
    files = os.listdir(directory)
    pattern = r'crypto_date_\d{4}-\d{2}-\d{2}'
    json_files = [f for f in files if re.search(pattern, f)]
    json_files.sort(reverse=True)
    latest_file = os.path.join(directory, json_files[0])
    file = open(latest_file)
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


def populate_crypto():
    for entry in parse_crypto():
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


def parse_metals():
    directory = "C:/Users/agafi/IdeaProjects/coinmarketcap_clone/clone/json_files"
    files = os.listdir(directory)
    pattern = r'metals_date_\d{4}-\d{2}-\d{2}'
    json_files = [f for f in files if re.search(pattern, f)]
    json_files.sort(reverse=True)
    latest_file = os.path.join(directory, json_files[0])
    #file = open(latest_file)

    with open(latest_file) as f:
        data = json.load(f)

    rates = data["rates"]

    metals = []
    for code, rate in rates.items():
        p = PreciousMetals(code, rate)
        metals.append(p)
    return metals

    #data = json.load(file)
    # result_metal = []
    # metals = []
    # for key, val in data["rates"].items():
    #     result_metal.append(key)
    #     result_metal.append(val)
    #     for i in range(0, len(result_metal), 2):
    #         code = result_metal[i]
    #         rate = result_metal[i+1]
    #         p = PreciousMetals(code, rate)
    #         metals.append(p)
    # print(metals)


def populate_metal():
    for e in parse_metals():
        code = e.code
        rate = e.rate

        metal_created = PreciousMetalsModel.objects.get_or_create(
            code=code, rate=rate)


if __name__ == '__main__':
    print("clearing database")
    call_command("flush", interactive=False)
    print("populating script!")
    populate_crypto()
    populate_metal()
    print("populating complete!!")
