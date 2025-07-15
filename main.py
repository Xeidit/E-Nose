'''
Jobs to do:
Connect to printer
get printer status
home z axis
home y axis
home x axis
'''


import requests

# Moonraker server Address
moonrakerUrl = "http://localhost:7125"

def init():
    # Get server status
    url = moonrakerUrl + "/printer/info" # Query server status
    try:
        response = requests.get(url)
        response.raise_for_status() # Raise an error for bad status codes
        data = response.json() # Parse JSON response
        print("Printer Info:", data) # Display response
    except requests.exceptions.RequestException as e:
        print("Request failed:", e) # Display error message if failed
        return e # Return error message


    # Send G-code
    # Replace with your Moonraker server's IP and port
    url = moonrakerUrl + "/printer/gcode/script"

    # G-code command to send (e.g., homing the printer)
    gcode_command = "G28"

    # Prepare the payload
    payload = {
        "script": gcode_command
    }

    try:
        response = requests.post(url, json=payload) # Send Request
        response.raise_for_status() # Raise an error for bad status codes
        print("Response:", response.json()) # Display response
    except requests.exceptions.RequestException as e:
        print("Request failed:", e) # Display error message if failed
        return e # Return error message