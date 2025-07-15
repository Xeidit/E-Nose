import requests


def post_with_error_handling(url, payload=None):
    try:
        if payload is None:
            response = requests.get(url)
        else:
            response = requests.post(url, json=payload) # Send Request
        response.raise_for_status() # Raise an error for bad status codes
        return response.json()
    except requests.exceptions.RequestException as e:
        print("Request failed:", e) # Display error message if failed
        return e # Return error message