import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'clone.settings')

django.setup()


import json
import datetime
import requests
from crypto import Crypto, PreciousMetals, News
from coin_app.models import CryptoModel, PreciousMetalsModel, NewsModel
from django.core.management import call_command


def get_crypto_data():
    url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest?CMC_PRO_API_KEY=3fa9c876-5dee-4ec7-95c6-d88ca297978c"
    headers = {
        'CMC_PRO_API_KEY': '3fa9c876-5dee-4ec7-95c6-d88ca297978c'
    }
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
            crypto_obj = Crypto(name, symbol, price, percent_change_24h,
                                percent_change_7d, market_cap, volume_24h,
                                circulating_supply)
            crypto_data.append(crypto_obj)
            print(crypto_obj)
        return crypto_data
    else:
        print("Request failed - crypto")
        return None


def populate_crypto():
    for entry in get_crypto_data():
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


def make_request_precious_metals():
    url = "https://api.metalpriceapi.com/v1/latest?api_key=a62cfed78fadac1191a9f88c82bb1faf&base=USD&currencies=XAG,XAU,XPD,XPT"

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
        return metals
    else:
        print("Request failed - metal")
        return None


def populate_metal():
    for e in make_request_precious_metals():
        code = e.code
        rate = e.rate

        metal_created = PreciousMetalsModel.objects.get_or_create(
            code=code, rate=rate)


def make_request_news():
    url = "https://newsapi.org/v2/everything?q=cryptocurrency&apiKey=51c8125aa88446f0a22818fef806e097"

    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)

    if response.status_code == 200:
        json_data = json.loads(response.text)
        news = []
        for i in json_data['articles']:
            published = datetime.datetime.strptime(i['publishedAt'], '%Y-%m-%dT%H:%M:%SZ').strftime('%Y-%m-%d')
            n = News(i['title'], i['author'], published, i['url'])
            news.append(n)
        return news
    else:
        print("Request failed - news")
        return None


def populate_news():
    for n in make_request_news():
        title = n.title
        author = n.author if n.author else 'Unknown'
        published = n.published
        url = n.url

        news_created = NewsModel.objects.get_or_create(
            title=title, author=author, published=published, url=url
        )


if __name__ == '__main__':
    print("clearing database")
    call_command("flush", interactive=False)
    get_crypto_data()
    make_request_precious_metals()
    make_request_news()
    make_request_news()
    print("populating script!")
    populate_crypto()
    populate_metal()
    populate_news()
    print("populating complete!!")
