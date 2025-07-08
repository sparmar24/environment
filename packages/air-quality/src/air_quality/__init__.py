import requests
import os
import json

def main() -> None: 
    APIKEY = os.environ.get("API_KEY") 
    url = f"https://airquality.googleapis.com/v1/currentConditions:lookup?key={APIKEY}"

    # JSON payload
    payload = {
        "location": {
            "latitude": 37.419734,
            "longitude": -122.0827784
        }
    }

    # HTTP headers
    headers = {
        "Content-Type": "application/json"
    }

    # Make the POST request
    response = requests.post(url, json=payload, headers=headers)

    # Print the response
    if response.status_code == 200:
        print(response.json())
    else:
        print("Error:", response.status_code, response.text)

    with open("air_quality_response.json", "w") as f:
        json.dump(response.json(), f, indent=4)
