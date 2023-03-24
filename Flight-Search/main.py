import requests
from prettytable import PrettyTable
import tkinter as tk

# Define the API endpoint
url = "https://test.api.amadeus.com/v1/security/oauth2/token"

# Authentication parameters
params = {
    "grant_type": "client_credentials",
    "client_id": "vbCW9wGpKPh2HI843Jw1KLVrWTJNAij5",
    "client_secret": "bYTGyJfS2a6uM6Cy"
}

#  Request for authentication token
response = requests.post(url, data=params)
access_token = ""
if response.status_code == 200:
    data = response.json()
    access_token = data["access_token"]
    # use the access token to make requests to the Amadeus API
else:
    print("Error:", response.status_code)

# Define the GUI window
root = tk.Tk()
root.title("Flight Search")

# Define the GUI elements
origin_label = tk.Label(root, text="Origin:")
origin_label.grid(row=0, column=0)
origin_entry = tk.Entry(root)
origin_entry.grid(row=0, column=1)

destination_label = tk.Label(root, text="Destination:")
destination_label.grid(row=1, column=0)
destination_entry = tk.Entry(root)
destination_entry.grid(row=1, column=1)

date_label = tk.Label(root, text="Date (YYYY-MM-DD):")
date_label.grid(row=2, column=0)
date_entry = tk.Entry(root)
date_entry.grid(row=2, column=1)

search_button = tk.Button(root, text="Search", command=lambda: get_flights())
search_button.grid(row=3, column=0)


# Define a function to get the flight offers
def get_flights():
    # Get the user input
    origin = origin_entry.get()
    destination = destination_entry.get()
    date = date_entry.get()

    new_params = {
        "originLocationCode": origin,
        "destinationLocationCode": destination,
        "departureDate": date,
        "adults": 1,
        "currencyCode": "GBP"
    }

    new_headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }

    new_url = "https://test.api.amadeus.com/v2/shopping/flight-offers"
    flight_response = requests.get(new_url, headers=new_headers, params=new_params)

    # Parse the API response and display the results
    if flight_response.status_code == 200:
        flight_data = flight_response.json()
        table = PrettyTable()
        table.field_names = ["Departure", "Arrival", "Duration", "Price"]
        for offer in flight_data["data"]:
            itinerary = offer["itineraries"][0]
            segments = itinerary["segments"]
            departure = segments[0]["departure"]["iataCode"]
            arrival = segments[-1]["arrival"]["iataCode"]
            duration = itinerary["duration"]
            price = offer["price"]["total"]
            table.add_row([departure, arrival, duration, price])
        results_label.config(text=table)
    else:
        results_label.config(text="Error: could not retrieve flight offers")


# Define the results label
results_label = tk.Label(root, text="")
results_label.grid(row=4, column=0, columnspan=2)

# Start the GUI mainloop
root.mainloop()
