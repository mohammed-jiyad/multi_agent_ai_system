import requests
import time

def get_next_launch(retries=1):
    url = "https://api.spacexdata.com/v4/launches/next"
    for attempt in range(retries):
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            data = response.json()
            return {
                "location": {
                    "name": data["launchpad"],
                    "latitude": 28.6080585,
                    "longitude": -80.6039558
                },
                "date": data["date_utc"]
            }
        except Exception as e:
            print(f"[Retry {attempt+1}] Launch API error: {e}")
            time.sleep(1)
    raise Exception("Failed to fetch launch data after retries.")
