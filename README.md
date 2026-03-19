🚴 AI Risk Engine for Delivery Workers

An AI-powered system that predicts real-time disruption risk for delivery workers using environmental data such as weather and air quality.

🌟 Problem Statement

Delivery workers (Zomato, Swiggy, gig workers) face income instability due to:

🌧 Sudden rain

🌫 Poor air quality

🚫 Reduced order demand during extreme conditions

Currently:

No real-time risk awareness

No predictive systems

No automated protection

👉 Result: Unpredictable earnings and financial stress

👤 Target User (Persona)
🎯 Primary User: Delivery Partner

Age: 18–40

Works on platforms like Zomato / Swiggy

Income depends on daily conditions

Needs predictable earnings

😔 Pain Points:

“Will I earn enough today?”

“Should I go out in bad weather?”

“No system warns me about risk”

💡 Solution

We built an AI Risk Engine that:

Predicts disruption risk in real-time

Uses environmental signals

Enables proactive decision-making

🤖 How the AI Works
Input Features:

🌧 Rainfall (mm)

🌫 AQI (Air Quality Index)

📍 Location (latitude, longitude)

Model:

Logistic Regression (Scikit-learn)

Output:

Risk Score (0 → 1)

Score	Meaning
0–0.4	Low Risk ✅
0.4–0.7	Medium Risk ⚠️
0.7–1	High Risk 🚨
🧠 AI Logic

The model learns patterns like:

High rain + poor AQI → High risk

Moderate conditions → Medium risk

Clear weather → Low risk

👉 Output = Probability of disruption

⚙️ System Architecture
User
  ↓
Location API (IP-based)
  ↓
Weather API + AQI API
  ↓
ML Model (Risk Prediction)
  ↓
Streamlit Dashboard
📡 How It Works (Flow)

User enters basic details

System detects location

Fetches:

Weather data

AQI data

ML model predicts risk score

UI displays:

Risk level

Environmental data

Live monitoring updates risk

🧠 Technical Implementation

Frontend: Streamlit

Backend: Python

ML: Logistic Regression (Scikit-learn)

APIs: OpenWeather, IP Geolocation

Data Handling: NumPy

Model Storage: Joblib

📉 Market Crash Relevance 🚨

During economic downturns:

Gig workers are most affected

Demand fluctuates unpredictably

Income instability increases

💥 Our Solution Helps By:

Predicting low-demand / high-risk periods

Allowing workers to:

Avoid unprofitable hours

Optimize working time

Enabling future automated insurance payouts

👉 This creates a financial safety layer for gig workers

🔮 Future Enhancements
📸 1. Photo-Based Risk Detection

Users upload real-time images

AI detects:

Rain intensity

Road conditions

Visibility

📍 2. Geo-Tagged Image Validation

Ensures:

Location authenticity

Fraud prevention

📈 3. Time-Series Prediction

Predict risk for next few hours

Use LSTM / sequence models

🔔 4. Alert System

Notify users:

“High risk in next 2 hours”

💳 5. Parametric Insurance

Auto payouts triggered by:

Environmental conditions

No manual claims

🏆 Use Cases

Delivery platforms (Zomato, Swiggy)

Gig worker protection systems

Insurance technology (InsurTech)

Smart city monitoring

🚀 How to Run
git clone https://github.com/CodeStartAI-009/guidwire.git
cd guidwire

python3 -m venv venv
source venv/bin/activate

pip install -r requirements.txt

export OPENWEATHER_API_KEY="your_api_key_here"

python ml/train_model.py

streamlit run app.py
⚠️ Notes

API keys must be valid and activated

Location is approximate (IP-based)

Fallback values used if API fails

👨‍💻 Author

Varun D
AI/ML Developer | Building real-world intelligent systems

⭐ Final Thought

“We are not just predicting risk — we are enabling financial stability for millions of gig workers.”