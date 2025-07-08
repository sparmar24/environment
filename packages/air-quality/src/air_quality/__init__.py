from pprint import pprint
import requests
import os
import json


def main() -> None:
    locations = [
        {"latitude": 37.419734, "longitude": -122.0827784},  # Mountain View, CA
        {"latitude": 34.052235, "longitude": -118.243683},  # Los Angeles, CA
        {"latitude": 40.712776, "longitude": -74.005974},  # New York, NY
    ]
    for location in locations:
        main_location(location)


def main_location(location: dict) -> None:
    APIKEY = os.environ.get("API_KEY")
    url = f"https://airquality.googleapis.com/v1/currentConditions:lookup?key={APIKEY}"

    # JSON payload
    payload = {"location": location}

    # HTTP headers
    headers = {"Content-Type": "application/json"}

    # Make the POST request
    response = requests.post(url, json=payload, headers=headers)

    # Print the response
    if response.status_code == 200:
        pprint(response.json())
    else:
        print("Error:", response.status_code, response.text)

    with open("air_quality_response.json", "w") as f:
        json.dump(response.json(), f, indent=4)
