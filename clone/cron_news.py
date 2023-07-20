import os
import django
import datetime
import requests
import json

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'clone.settings')
django.setup()

from coin_app.models import NewsModel
from decouple import config
from crypto import News

def populate_news():
    NewsModel.objects.all().delete()
    url = config('URL_NEWS')

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
        for entry in news:
            title = entry.title
            author = entry.author if entry.author else 'Unknown'
            published = entry.published
            url = entry.url

            NewsModel.objects.update_or_create(
                title=title, author=author, published=published, url=url
            )
    else:
        print("Request failed - news")

if __name__ == '__main__':
    populate_news()
