'''
Jobs to do:
Connect to printer
get printer status
home z axis
home y axis
home x axis
'''

import requests
from standard_functions import probe
from standard_functions import g_code

x_offset = 64 # Offset to first bottle (bottom left) in the x direction
y_offset = 28 # Offset to first bottle (bottom left) in the y direction

# Moonraker server Address
moonrakerUrl = "http://10.0.0.1:7125"


def init():
    # Get server status
    url = moonrakerUrl + "/printer/info"  # Query server status
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad status codes
        data = response.json()  # Parse JSON response
        #print("Printer Info:", data)  # Display response
    except requests.exceptions.RequestException as e:
        print("Request failed:", e)  # Display error message if failed
        return e  # Return error message
    g_code(moonrakerUrl, "g28") #Homes Z axis
    offset = "x"+str(x_offset)+"y"+str(y_offset) + "z340" 
    g_code(moonrakerUrl, "g1"+offset + "F2000") #moves over first bottle
    g_code(moonrakerUrl, "g92 x0 y0") #re allign axis over first bottle
    return "Printer Ready"

init()
probe(moonrakerUrl,[1,0,250]) # Probe bottle [X,Y,Z height in mm] index from 0
probe(moonrakerUrl,[3,0,250]) # Probe bottle [X,Y,Z height in mm] index from 0
probe(moonrakerUrl,[5,0,250]) # Probe bottle [X,Y,Z height in mm] index from 0
probe(moonrakerUrl,[7,0,250]) # Probe bottle [X,Y,Z height in mm] index from 0
