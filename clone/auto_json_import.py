import schedule
import time
import requests
import json
import datetime
import os


def make_request():
    url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest?CMC_PRO_API_KEY=3fa9c876-5dee-4ec7-95c6-d88ca297978c"

    current_time = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M")
    folder_path = "C:/Users/agafi/IdeaProjects/coinmarketcap_clone/clone/json_files"
    file_name = f"data_{current_time}.json"
    file_path = f"{folder_path}/{file_name}"
    payload = {}
    headers = {
        'CMC_PRO_API_KEY': '3fa9c876-5dee-4ec7-95c6-d88ca297978c'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    if response.status_code == 200:
        print(response.text)
        with open(file_path, "w") as outfile:
            json.dump(response, outfile)
    else:
        print("Request failed")


def schedule_task():
    schedule.every(10).seconds.do(make_request)
    #schedule.every(10).minutes.do(make_request)

    while True:
        schedule.run_pending()
        time.sleep(1)

# start the scheduler when the app is ready
schedule_task()

# start the scheduler when the app is ready
# def ready(self):
#     super().ready()
#     schedule_task()