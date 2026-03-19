import requests
from config import API_KEY


def get_weather(lat, lon):
    """
    Fetch real-time weather data from OpenWeather API

    Returns:
        rain (float): rainfall in mm (last 1 hour)
        temp (float): temperature in Celsius
    """

    url = (
        f"https://api.openweathermap.org/data/2.5/weather"
        f"?lat={lat}&lon={lon}&appid={API_KEY}&units=metric"
    )

    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        data = response.json()

        # 🌧 Rain (may not exist → default 0)
        rain = 0
        if "rain" in data and "1h" in data["rain"]:
            rain = data["rain"]["1h"]

        # 🌡 Temperature
        temp = data["main"]["temp"]

        return rain, temp

    except requests.exceptions.RequestException as e:
        print("❌ Weather API error:", e)
        return 0, 25  # fallback values

    except KeyError as e:
        print("❌ Unexpected API response:", e)
        return 0, 25