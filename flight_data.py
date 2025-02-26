class FlightData:
    #This class is responsible for structuring the flight data.

    def __init__(self, price, origin_airport, destination_airport, out_date, return_date):
        """Initializing new flight data to a specific location"""
        self.price = price
        self.origin_airport = origin_airport
        self.destination_airport = destination_airport
        self.out_date = out_date
        self.return_date = return_date

    def finding_cheapest(data):
        """Using Amadeus API to find the cheapest flight (all locations)"""

        #When no flight is found (no data)
        if data is None or not data['data']:
            print("No flight data")
            return FlightData("N/A", "N/A", "N/A", "N/A", "N/A")

        #Data for the first flight in the json data file
        first_flight = data['data'][0]
        lowest_price = float(first_flight["price"]["grandTotal"])
        origin = first_flight["itineraries"][0]["segments"][0]["departure"]["iataCode"]
        destination = first_flight["itineraries"][0]["segments"][0]["arrival"]["iataCode"]
        date_out = first_flight["itineraries"][0]["segments"][0]["departure"]["at"].split("T")[0]
        date_return = first_flight["itineraries"][1]["segments"][0]["departure"]["at"].split("T")[0]

        # Initialize FlightData class with the first flight, comparing if it is cheapest
        cheapest_flight = FlightData(lowest_price, origin, destination, date_out, date_return)

        for flight in data["data"]:
            price = float(flight["price"]["grandTotal"])
            if price < lowest_price:
                lowest_price = price
                origin = flight["itineraries"][0]["segments"][0]["departure"]["iataCode"]
                destination = flight["itineraries"][0]["segments"][0]["arrival"]["iataCode"]
                out_date = flight["itineraries"][0]["segments"][0]["departure"]["at"].split("T")[0]
                return_date = flight["itineraries"][1]["segments"][0]["departure"]["at"].split("T")[0]
                cheapest_flight = FlightData(lowest_price, origin, destination, out_date, return_date)
                print(f"The lowest price to {destination} is £{lowest_price}")

        return cheapest_flight

