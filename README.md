# 🚴 AI Risk Engine for Delivery Workers

An AI-powered system that predicts real-time disruption risk for delivery workers using environmental data like weather and air quality.

---

## 🌟 Overview

Delivery workers often lose income due to unpredictable conditions such as heavy rain or poor air quality.

This project builds a **real-time risk prediction engine** that:
- Fetches environmental data (weather + AQI)
- Uses a machine learning model
- Predicts disruption risk dynamically

---

## ⚡ Features

- 🌧 Real-time Weather Analysis (Rainfall, Temperature)
- 🌫 Air Quality Index (AQI) Monitoring
- 📍 Location Detection (IP-based)
- 🤖 Machine Learning Risk Prediction (Logistic Regression)
- 📡 Live Risk Monitoring Dashboard (Streamlit)
- 🔁 Refresh-based real-time updates

---

## 🧠 Tech Stack

- **Frontend/UI:** Streamlit  
- **Backend:** Python  
- **ML Model:** Scikit-learn (Logistic Regression)  
- **APIs:** OpenWeather API, IP Geolocation API  
- **Libraries:** NumPy, Requests, Joblib  

---

## 🏗 Project Structure


guidwire/
│
├── app.py
├── config.py
├── requirements.txt
│
├── services/
│ ├── weather.py
│ ├── aqi.py
│ ├── location.py
│
├── ml/
│ ├── model.py
│ ├── train_model.py
│
├── utils/
│ ├── helpers.py
│
└── venv/


---

## 🚀 How to Run

### 1. Clone the repo

git clone https://github.com/your-username/guidwire.git

cd guidwire


---

### 2. Create virtual environment

python3 -m venv venv
source venv/bin/activate


---

### 3. Install dependencies

pip install -r requirements.txt


---

### 4. Set API key

export OPENWEATHER_API_KEY="your_api_key_here"


---

### 5. Train model (one-time)

python ml/train_model.py


---

### 6. Run the app

streamlit run app.py


---

## 📊 How It Works

1. User enters basic details  
2. System detects location  
3. Fetches:
   - Weather data  
   - AQI data  
4. ML model predicts risk score  
5. UI displays:
   - Risk level  
   - Environmental conditions  
6. Live monitoring updates risk dynamically  

---

## 🧠 Machine Learning

- Model: Logistic Regression  
- Features:
  - Rainfall (mm)
  - AQI (1–5)
- Output:
  - Risk probability (0–1)

---

## 🔮 Future Enhancements

- 📸 Photo-based risk detection using computer vision  
- 📍 Geo-tagged image validation for fraud prevention  
- 📈 Time-series risk prediction (LSTM)  
- 🔔 Real-time alert system  
- 💳 Automated parametric insurance payouts  

---

## 🏆 Use Cases

- Delivery platforms (Zomato, Swiggy)
- Gig worker protection systems
- Insurance tech (InsurTech)
- Smart city risk monitoring

---

## ⚠️ Notes

- API keys must be valid and activated  
- Fallback values can be used if APIs fail  
- Location is approximate (IP-based)

---

## 👨‍💻 Author

Varun D  
AI/ML Developer | Building real-world intelligent systems

---

## ⭐ If you like this project

Give it a star ⭐ on GitHub!# Guidwire
