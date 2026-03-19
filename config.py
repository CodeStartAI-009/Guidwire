import os

# Load API key from environment variable
API_KEY = os.getenv("OPENWEATHER_API_KEY")

if API_KEY is None:
    raise ValueError("❌ OPENWEATHER_API_KEY not set. Please export it before running.")