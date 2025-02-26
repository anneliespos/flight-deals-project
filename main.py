#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

import time
from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData
from datetime import datetime, timedelta
from notification_manager import NotificationManager

data_manager=DataManager
sheet_data = data_manager.get_data()
flight_search = FlightSearch
notification_manager = NotificationManager

ORIGIN_CITY= "LON"      #using London as hometown to fly from


#-----------Update IATA codes to the real IATA codes -----------

for row in sheet_data:
    if row["iataCode"] == "":
        row["iataCode"] = flight_search.get_code(row["city"])
        # slowing down requests to avoid rate limit
        time.sleep(2)
    print(f"sheet_data:\n {sheet_data}")

    data_manager.destination_data = sheet_data
    data_manager.update_iata_codes()


#----------Searching for flights --------------
tomorrow = datetime.now() + timedelta(days=1)
six_months = datetime.now() + timedelta(days=(6 * 30))

for destination in sheet_data:
    print(f"Searching flights for {destination['city']}...")
    flights = flight_search.check_flights(
        origin_city_code=ORIGIN_CITY,
        destination_city_code=destination["iataCode"],
        from_time=tomorrow,
        to_time=six_months
    )
    cheapest_flight = FlightData.finding_cheapest(flights)

    if cheapest_flight.price != "N/A" and cheapest_flight.price < destination["lowestPrice"]:
        print(f"Lower price flight found to {destination['city']}!")
        notification_manager.send_sms(
            message_body=f"Good flight deal found! The flight from {cheapest_flight.origin_airport} "
                         f"to {cheapest_flight.destination_airport}, on {cheapest_flight.out_date} "
                         f"until {cheapest_flight.return_date}, is now £{cheapest_flight.price}."
        )



