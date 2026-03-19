import requests


def get_location():
    """
    Fetch approximate user location using IP-based geolocation

    Returns:
        lat (float)
        lon (float)
        city (str)
    """

    url = "http://ip-api.com/json"

    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        data = response.json()

        lat = data.get("lat", 0.0)
        lon = data.get("lon", 0.0)
        city = data.get("city", "Unknown")

        return lat, lon, city

    except requests.exceptions.RequestException as e:
        print("❌ Location API error:", e)
        return 0.0, 0.0, "Unknown"

    except KeyError as e:
        print("❌ Unexpected location response:", e)
        return 0.0, 0.0, "Unknown"