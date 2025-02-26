import requests
import os
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv

load_dotenv()

SHEETY_ENDPOINT = "TYPE ENDPOINT"

class DataManager:
    #This class is responsible for talking to the Google Sheet.

    def __init__(self):
        self.user = os.environ["SHEETY_USERNAME"]
        self.password = os.environ["SHEETY_PASSWORD"]
        self.authorization = HTTPBasicAuth(self.user, self.password)
        self.destination_data={}

    def get_data(self):
    # 2 Use Sheety to GET all the data in that sheet and print it out
        response = requests.get(url=SHEETY_ENDPOINT)
        data= response.json()
        self.destination_data= data["prices"]
        return self.destination_data

    def update_iata_codes(self):
    #6. make  PUT request, use the row id from sheet_data, update Google Sheet with  IATA codes
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_ENDPOINT}/{city['id']}",
                json=new_data,
                auth=self.authorization
            )
            print(response.text)