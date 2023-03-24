from tkinter import *
from tkinter import ttk
from tkcalendar import DateEntry
import requests

airports = {
    'Aberdeen': 'ABZ',
    'Bacau': 'BCM',
    'Belfast': 'BFS',
    'Birmingham': 'BHX',
    'Bristol': 'BRS',
    'Cardiff': 'CWL',
    'Derry': 'LDY',
    'Doncaster Sheffield': 'DSA',
    'Dublin': 'DUB',
    'Durham Tees Valley': 'MME',
    'East Midlands': 'EMA',
    'Edinburgh': 'EDI',
    'Exeter': 'EXT',
    'Glasgow': 'GLA',
    'Guernsey': 'GCI',
    'Inverness': 'INV',
    'Isle of Man': 'IOM',
    'Jersey': 'JER',
    'Leeds Bradford': 'LBA',
    'Liverpool': 'LPL',
    'London City': 'LCY',
    'London Gatwick': 'LGW',
    'London Heathrow': 'LHR',
    'London Luton': 'LTN',
    'London Stansted': 'STN',
    'Manchester': 'MAN',
    'Newcastle': 'NCL',
    'Newquay': 'NQY',
    'Norwich': 'NWI',
    'Southampton': 'SOU',
    'Amsterdam': 'AMS',
    'Athens': 'ATH',
    'Barcelona': 'BCN',
    'Berlin': 'TXL',
    'Brussels': 'BRU',
    'Budapest': 'BUD',
    'Copenhagen': 'CPH',
    'Frankfurt': 'FRA',
    'Geneva': 'GVA',
    'Istanbul': 'IST',
    'Lisbon': 'LIS',
    'Madrid': 'MAD',
    'Milan': 'MXP',
    'Moscow': 'SVO',
    'Munich': 'MUC',
    'Oslo': 'OSL',
    'Paris': 'CDG',
    'Prague': 'PRG',
    'Rome': 'FCO',
    'Stockholm': 'ARN',
    'Vienna': 'VIE',
    'Warsaw': 'WAW',
    'Zurich': 'ZRH',
    'Bucharest': 'OTP',
    'Cluj-Napoca': 'CLJ',
    'Constanța': 'CND',
    'Iași': 'IAS',
    'Oradea': 'OMR',
    'Sibiu': 'SBZ',
    'Timișoara': 'TSR',
    'Sofia': 'SOF',
    'Burgas': 'BOJ',
    'Plovdiv': 'PDV',
    'Varna': 'VAR',
    'Bangkok': 'BKK',
    'Beijing': 'PEK',
    'Dubai': 'DXB',
    'Hong Kong': 'HKG',
    'Kuala Lumpur': 'KUL',
    'Manila': 'MNL',
    'Mumbai': 'BOM',
    'New Delhi': 'DEL',
    'Seoul': 'ICN',
    'Shanghai': 'PVG',
    'Singapore': 'SIN',
    'Taipei': 'TPE',
    'Tokyo': 'HND',
    'Islamabad': 'ISB',
    'Karachi': 'KHI',
    'Lahore': 'LHE',
    'Multan': 'MUX',
    'Peshawar': 'PEW',
    'Quetta': 'UET'
}
airports_sorted = dict(sorted(airports.items()))
airport_names = list(airports_sorted.keys())


# Function to retrieve airport full name based on IATA code from dictionary
def get_airport_name(iata_code):
    for key, value in airports_sorted.items():
        if iata_code == value:
            return key


# Creating application canvas
canvas = Tk()

# Creating a ttk style object
style = ttk.Style()

# Setting application title
canvas.title("Flight Search")

# Setting application background
canvas.configure(background="#F0EAD6")  # Eggshell colour 	#F0EAD6

# Minimum size of application window
canvas.minsize(800, 800)

# Maximum size of application window
canvas.maxsize(1024, 1024)

# Creating frame for header image and heading
header_frame = Frame(canvas, bg="#F0EAD6", height=150, width=canvas.winfo_width())
header_frame.pack(side=TOP, fill=X)

# Header image
header_img = PhotoImage(file="plane.png")

# Resizing header image
header_img = header_img.subsample(3, 3)

# Creating a transparent label for the header image
img = Label(header_frame, image=header_img, bg="#F0EAD6")
img.image = header_img  # to prevent image from being garbage collected
img.pack(side=LEFT)

# Heading label
heading = Label(header_frame, text="Flight Search", font=("Montserrat", 30), bg="#F0EAD6")
heading.pack(side=LEFT)

# Creating main frame for the rest of the application
main_frame = Frame(canvas, bg="#F0EAD6")
main_frame.pack(side=TOP, fill=BOTH, expand=True)

# Creating menu frame on the left side of the main frame
menu_frame = Frame(main_frame, bg="#F0EAD6", width=150)
menu_frame.pack(side=LEFT, fill=Y)

# Creating dropdown for 'From' cities
from_label = Label(menu_frame, text="From:", font=("Futura", 16), bg="#F0EAD6")
from_label.pack(side=TOP, pady=10)
from_var = StringVar()
from_dropdown = ttk.Combobox(menu_frame, textvariable=from_var, values=airport_names, font=("Arial", 14))
from_dropdown.pack(side=TOP, pady=5)

# Creating dropdown for 'To' cities
to_label = Label(menu_frame, text="To:", font=("Futura", 16), bg="#F0EAD6")
to_label.pack(side=TOP, pady=10)
to_var = StringVar()
to_dropdown = ttk.Combobox(menu_frame, textvariable=to_var, values=airport_names, font=("Arial", 14))
to_dropdown.pack(side=TOP, pady=5)

# Creating date selector for flight date
date_label = Label(menu_frame, text="Flight Date:", font=("Futura", 16), bg="#F0EAD6")
date_label.pack(side=TOP, pady=10)
date_picker = DateEntry(menu_frame, width=12, background='white', foreground='black', borderwidth=2)
date_picker.pack(side=TOP, pady=5)
# selected_date = date_picker.get_date()


# Creating main frame on the right side of the main frame
main_content_frame = Frame(main_frame, bg="#F0EAD6")
main_content_frame.pack(side=LEFT, fill=BOTH, expand=True)

# Creating result frame for displaying search results
result_frame = Frame(main_content_frame, bg="#9DC3E6")
result_frame.pack(side=TOP, fill=BOTH, expand=True, padx=50, pady=50)

# Creating result label
result_label = Label(result_frame, text="Results:", font=("Futura", 14), bg="#9DC3E6")
result_label.pack(side=TOP, pady=10)

# Creating a scrollbar for the result frame
result_scrollbar = Scrollbar(result_frame)
result_scrollbar.pack(side=RIGHT, fill=Y)

# Creating a treeview to display the search results
result_treeview = ttk.Treeview(result_frame, columns=("departure", "arrival", "duration", "price"), show="headings")
result_treeview.pack(side=LEFT, fill=BOTH, expand=True)

# Defining the column headings and widths
result_treeview.heading("departure", text="Departure", anchor="w")
result_treeview.column("departure", width=150, anchor="w")

result_treeview.heading("arrival", text="Arrival", anchor="w")
result_treeview.column("arrival", width=150, anchor="w")

result_treeview.heading("duration", text="Duration", anchor="w")
result_treeview.column("duration", width=150, anchor="w")

result_treeview.heading("price", text="Price", anchor="w")
result_treeview.column("price", width=150, anchor="w")

# Applying CSS styles to the treeview
style.configure("ResultTreeview.Treeview", background="white", fieldbackground="white", font=("Futura", 12),
                foreground="#4B4E6D", rowheight=30)

style.map("ResultTreeview.Treeview", background=[("selected", "#9DC3E6")])


def search_flight():
    # Define the authentication API endpoint
    url = "https://test.api.amadeus.com/v1/security/oauth2/token"

    # Authentication parameters
    params = {
        "grant_type": "client_credentials",
        "client_id": "vbCW9wGpKPh2HI843Jw1KLVrWTJNAij5",
        "client_secret": "bYTGyJfS2a6uM6Cy"
    }

    #  Request for authentication token
    response = requests.post(url, data=params)

    # Defining access_token outside if block to make it accessible everywhere
    access_token = ""
    if response.status_code == 200:
        data = response.json()
        access_token = data["access_token"]
        # use the access token to make requests to the Amadeus API
    else:
        result_treeview.insert("", "end", values=(f"Error: {response.status_code}", "", "", ""))

    new_params = {
        "originLocationCode": airports_sorted[from_var.get()],
        "destinationLocationCode": airports_sorted[to_var.get()],
        "departureDate": date_picker.get_date(),
        "adults": 1,
        "currencyCode": "GBP",
        "max": 25  # limit the number of results to 15
    }

    new_headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }

    new_url = "https://test.api.amadeus.com/v2/shopping/flight-offers"
    flight_response = requests.get(new_url, headers=new_headers, params=new_params)

    # Adding the search results to the treeview
    if flight_response.status_code == 200:
        flight_data = flight_response.json()
        for offer in flight_data["data"]:
            itinerary = offer["itineraries"][0]
            segments = itinerary["segments"]
            departure = segments[0]["departure"]["iataCode"]
            departure = get_airport_name(departure)
            arrival = segments[-1]["arrival"]["iataCode"]
            arrival = get_airport_name(arrival)
            duration = itinerary["duration"][2:]
            price = offer["price"]["total"]
            result_treeview.insert("", "end", values=(departure, arrival, duration, price))
    else:
        result_treeview.insert("", "end", values=(f"Error: {flight_response.status_code}", "", "", ""))


# Creating search button
search_button = Button(menu_frame, text="Search", font=("Futura", 16), bg="#4B4E6D", fg="white", command=search_flight)
search_button.pack(side=TOP, pady=10)

# Starting the application loop
canvas.mainloop()