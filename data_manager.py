import requests
import os
from pprint import pprint
from dotenv import load_dotenv
load_dotenv()


SHEETY_PRICES_ENDPOINT = "https://api.sheety.co/5a510fcbe773445a1f66413c0c7b2f57/flightDeals/prices"
HEADERS = {
    "Authorization": os.getenv("sheety_authorization"),
}


class DataManager:

    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(
            url=SHEETY_PRICES_ENDPOINT, headers=HEADERS)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                json=new_data, headers=HEADERS
            )
            print(response.text)
