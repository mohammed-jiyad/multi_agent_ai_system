import requests
import os
import time

def get_weather_at_location(location, retries=1):
    lat = location["latitude"]
    lon = location["longitude"]
    api_key = os.getenv("WEATHER_API_KEY")
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units=metric"

    for attempt in range(retries):
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            return response.json()
        except Exception as e:
            print(f"[Retry {attempt+1}] Weather API error: {e}")
            time.sleep(1)
    raise Exception("Failed to fetch weather data after retries.")
