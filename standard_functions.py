import requests


safe_z_height = str(300) # Safe height for the head to move around at without the poker hitting bottles
def probe(url,bottle):
    x_pos = bottle[0]*56
    y_pos = bottle[1]*56
    z_pos = bottle[2]

    g_code(url, "g0 z"+ safe_z_height +"F1200") #Moves clear of bottles
    g_code(url, "g0 x"+ str(x_pos) + "y"+ str(y_pos) + "F2200") #Move over bottle to probe
    g_code(url, "g0 z"+ str(z_pos) +"F1200") #Move over bottle to probe

    return "ok"



def g_code(moonrakerurl,command):
    url = moonrakerurl + "/printer/gcode/script"

    payload = {
        "script": command
    }

    try:
        response = requests.post(url, json=payload) # Send Request
        response.raise_for_status() # Raise an error for bad status codes
        #print("Response:", response.json()) # Display response
        return response
    except requests.exceptions.RequestException as e:
        print("Request failed:", e) # Display error message if failed
        return e # Return error message
    


