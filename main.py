'''
Jobs to do:
Connect to printer
get printer status
home z axis
home y axis
home x axis
'''


import requests

from helpers import post_with_error_handling

# Moonraker server Address
moonrakerUrl = "http://10.0.0.1:7125"

def init():
    # Get server status
    url = moonrakerUrl + "/printer/info" # Query server status
    response = post_with_error_handling(url)
    if response['result']['state'] is not

    

def command(command):
    # Send G-code
    # Replace with your Moonraker server's IP and port
    url = moonrakerUrl + "/printer/gcode/script"

    # G-code command to send (e.g., homing the printer)
    gcode_command = command

    # Prepare the payload
    payload = {
        "script": gcode_command
    }


    response = post_with_error_handling(url)


    

init()
