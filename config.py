import os

try:
    import streamlit as st
    API_KEY = os.getenv("OPENWEATHER_API_KEY") or st.secrets.get("OPENWEATHER_API_KEY")
except Exception:
    API_KEY = os.getenv("OPENWEATHER_API_KEY")

if not API_KEY:
    API_KEY = "demo"  # fallback to prevent crash