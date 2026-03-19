import streamlit as st

# Import services
from services.weather import get_weather
from services.aqi import get_aqi
from services.location import get_location

# Import ML model
from ml.model import predict_risk

# Import helper
from utils.helpers import risk_label

st.set_page_config(page_title="AI Risk Engine", layout="centered")

st.title("🚴 AI Risk Engine for Delivery Workers")

# -------------------------------
# SESSION INIT
# -------------------------------
if "step" not in st.session_state:
    st.session_state.step = 1

# -------------------------------
# STEP 1: USER INPUT
# -------------------------------
if st.session_state.step == 1:
    st.header("👤 Enter Details")

    name = st.text_input("Name")
    platform = st.selectbox("Platform", ["Zomato", "Swiggy"])

    if st.button("Start Analysis"):
        st.session_state.name = name
        st.session_state.platform = platform
        st.session_state.step = 2

# -------------------------------
# STEP 2: REAL-TIME RISK ANALYSIS
# -------------------------------
elif st.session_state.step == 2:
    st.header("🌍 Real-Time Risk Analysis")

    with st.spinner("Fetching live data..."):
        lat, lon, city = get_location()
        rain, temp = get_weather(lat, lon)
        aqi = get_aqi(lat, lon)
        risk_score = predict_risk(rain, aqi)

    # Store for next step
    st.session_state.risk_score = risk_score
    st.session_state.city = city
    st.session_state.rain = rain
    st.session_state.temp = temp
    st.session_state.aqi = aqi

    # Display
    st.subheader(f"📍 Location: {city}")
    st.write(f"🌧 Rainfall: {rain} mm")
    st.write(f"🌡 Temperature: {temp} °C")
    st.write(f"🌫 AQI Level: {aqi}")

    st.progress(risk_score)

    label = risk_label(risk_score)

    if label == "HIGH":
        st.error("🚨 HIGH RISK")
    elif label == "MEDIUM":
        st.warning("⚠️ MEDIUM RISK")
    else:
        st.success("✅ LOW RISK")

    if st.button("Start Live Monitoring"):
        st.session_state.step = 3

# -------------------------------
# STEP 3: LIVE MONITORING LOOP
# -------------------------------
elif st.session_state.step == 3:
    st.header("📡 Live Risk Monitoring")

    refresh = st.button("🔄 Refresh Data")

    if refresh:
        with st.spinner("Updating data..."):
            lat, lon, city = get_location()
            rain, temp = get_weather(lat, lon)
            aqi = get_aqi(lat, lon)
            risk_score = predict_risk(rain, aqi)

            # Update session
            st.session_state.risk_score = risk_score
            st.session_state.city = city
            st.session_state.rain = rain
            st.session_state.temp = temp
            st.session_state.aqi = aqi

    # Display current state
    st.subheader(f"📍 {st.session_state.city}")
    st.write(f"🌧 Rain: {st.session_state.rain} mm")
    st.write(f"🌡 Temp: {st.session_state.temp} °C")
    st.write(f"🌫 AQI: {st.session_state.aqi}")

    st.progress(st.session_state.risk_score)

    label = risk_label(st.session_state.risk_score)

    if label == "HIGH":
        st.error("🚨 High Disruption Risk")
    elif label == "MEDIUM":
        st.warning("⚠️ Moderate Risk")
    else:
        st.success("✅ Safe Conditions")

    st.info("📊 Risk updates based on real-time environmental data")

    if st.button("Restart"):
        st.session_state.step = 1