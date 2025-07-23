'''
Jobs to do:
Connect to printer
get printer status
home z axis
home y axis
home x axis
'''

import requests
from standard_fuctions import g_code

# Moonraker server Address
moonrakerUrl = "http://localhost:7125"


def init():
    # Get server status
    url = moonrakerUrl + "/printer/info"  # Query server status
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad status codes
        data = response.json()  # Parse JSON response
        print("Printer Info:", data)  # Display response
    except requests.exceptions.RequestException as e:
        print("Request failed:", e)  # Display error message if failed
        return e  # Return error message

    g_code(moonrakerUrl, "g28 z") #Homes Z axis
    g_code(moonrakerUrl, "g28 x y") #Homes x and y axis
    g_code(moonrakerUrl, "g21") #Set units to mm

    g_code(moonrakerUrl,"g54") # Offset to first bottle
    return "Printer Ready"
