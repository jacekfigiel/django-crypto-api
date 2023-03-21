import schedule
import time
import requests
import json
import datetime
import os


def make_request_crypto():
    url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest?CMC_PRO_API_KEY=3fa9c876-5dee-4ec7-95c6-d88ca297978c"

    current_time = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M")
    folder_path = "C:/Users/agafi/IdeaProjects/coinmarketcap_clone/clone/json_files"
    file_name = f"crypto_date_{current_time}.json"
    file_path = f"{folder_path}/{file_name}"
    payload = {}
    headers = {
        'CMC_PRO_API_KEY': '3fa9c876-5dee-4ec7-95c6-d88ca297978c'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    if response.status_code == 200:
        json_data = json.loads(response.text)
        with open(file_path, "w") as outfile:
            json.dump(json_data, outfile)
    else:
        print("Request failed")


def make_request_precious_metals():
    url = "https://api.metalpriceapi.com/v1/latest?api_key=a62cfed78fadac1191a9f88c82bb1faf&base=USD&currencies=XAG,XAU,XPD,XPT"

    current_time = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M")
    folder_path = "C:/Users/agafi/IdeaProjects/coinmarketcap_clone/clone/json_files"
    file_name = f"metals_date_{current_time}.json"
    file_path = f"{folder_path}/{file_name}"
    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)

    if response.status_code == 200:
        json_data = json.loads(response.text)
        with open(file_path, "w") as outfile:
            json.dump(json_data, outfile)
    else:
        print("Request failed")


make_request_precious_metals()
make_request_crypto()
# def schedule_task():
#     #schedule.every(10).minutes.do(make_request)
#
#     while True:
#         schedule.run_pending()
#         time.sleep(1)
#
# # start the scheduler when the app is ready
# schedule_task()
#
# # start the scheduler when the app is ready
# # def ready(self):
# #     super().ready()
# #     schedule_task()