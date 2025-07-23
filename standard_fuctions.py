import requests

def g_code(moonrakerurl,command):
    url = moonrakerurl + "/printer/gcode/script"

    payload = {
        "script": command
    }

    try:
        response = requests.post(url, json=payload) # Send Request
        response.raise_for_status() # Raise an error for bad status codes
        print("Response:", response.json()) # Display response
        return response
    except requests.exceptions.RequestException as e:
        print("Request failed:", e) # Display error message if failed
        return e # Return error message