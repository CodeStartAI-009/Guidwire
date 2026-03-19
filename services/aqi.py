import requests
from config import API_KEY


def get_aqi(lat, lon):
    """
    Fetch Air Quality Index (AQI) from OpenWeather API

    Returns:
        aqi (int): AQI level (1–5 scale)
                   1 = Good
                   2 = Fair
                   3 = Moderate
                   4 = Poor
                   5 = Very Poor
    """

    url = (
        f"http://api.openweathermap.org/data/2.5/air_pollution"
        f"?lat={lat}&lon={lon}&appid={API_KEY}"
    )

    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        data = response.json()

        aqi = data["list"][0]["main"]["aqi"]

        return aqi

    except requests.exceptions.RequestException as e:
        print("❌ AQI API error:", e)
        return 2  # fallback (moderate)

    except (KeyError, IndexError) as e:
        print("❌ Unexpected AQI response:", e)
        return 2