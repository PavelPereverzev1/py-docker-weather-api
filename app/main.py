import os
import requests


def get_weather() -> None:

    API_KEY = os.getenv("API_KEY")
    if not API_KEY:
        print("Error: API_KEY is not set!")
        return

    CITY = "Paris"
    URL = (
        f"http://api.weatherapi.com/v1/current.json"
        f"?key={API_KEY}&q={CITY}&aqi=no"
    )

    try:
        response = requests.get(URL)
        response.raise_for_status()
        data = response.json()

        location = data["location"]
        current = data["current"]
        print(f"Performing request to Weather API for city {CITY}...")
        print(
            f"{location['name']}/{location['country']}"
            f" {location['localtime']} "
            f"Weather: {current['temp_c']} Celsius,"
            f" {current['condition']['text']}"
        )

    except Exception as error:
        print(f"An error occurred: {error}")


if __name__ == "__main__":
    get_weather()
