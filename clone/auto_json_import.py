import schedule
import time
import requests
import json


def make_request():
    url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest?CMC_PRO_API_KEY=3fa9c876-5dee-4ec7-95c6-d88ca297978c"

    payload = {}
    headers = {
        'CMC_PRO_API_KEY': '3fa9c876-5dee-4ec7-95c6-d88ca297978c'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    if response.status_code == 200:
        print(response.text)
        with open("simple.json", "w") as outfile:
            json.dump(response, outfile)
    else:
        print("Request failed")


def schedule_task():
    schedule.every(1).minutes.do(make_request)

    while True:
        schedule.run_pending()
        time.sleep(1)

# start the scheduler when the app is ready
schedule_task()
