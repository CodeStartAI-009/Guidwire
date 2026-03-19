# 🚴 AI Risk Engine for Delivery Workers

An AI-powered system that predicts real-time disruption risk for delivery workers using environmental data such as weather 🌧️ and air quality 🌫️.

## 🌟 Problem Statement

Delivery workers (Zomato, Swiggy, gig workers) face income instability due to:

- 🌧️ Sudden rain
- 🌫️ Poor air quality
- 📉 Reduced order demand during extreme conditions

### ❌ Current Issues

- No real-time risk awareness
- No predictive systems
- No automated financial protection

**👉 Result:** Unpredictable earnings and financial stress

## 👤 Target User (Persona)

**🎯 Primary User:** Delivery Partner

- **Age:** 18–40
- **Platform:** Works on Zomato / Swiggy
- **Income Model:** Depends on daily conditions
- **Need:** Predictable earnings

### 😔 Pain Points

- "Will I earn enough today?"
- "Should I go out in bad weather?"
- "No system warns me about risk"

## 💡 Solution

We built an AI Risk Engine that:

- 🔮 Predicts disruption risk in real-time
- 🌍 Uses environmental signals
- ⚡ Enables proactive decision-making

## 🤖 How the AI Works

### 📥 Input Features

- 🌧️ Rainfall (mm)
- 🌫️ AQI (Air Quality Index)
- 📍 Location (Latitude, Longitude)

### 🧠 Model

```python
from sklearn.linear_model import LogisticRegression

model = LogisticRegression()
```

### 📊 Output: Risk Score (0 → 1)

| Score Range | Meaning |
|---|---|
| 0.0 – 0.4 | Low Risk ✅ |
| 0.4 – 0.7 | Medium Risk ⚠️ |
| 0.7 – 1.0 | High Risk 🚨 |

### 🧠 AI Logic

The model learns patterns such as:

| Condition | Risk Level |
|---|---|
| High rainfall + poor AQI | High risk |
| Moderate conditions | Medium risk |
| Clear weather | Low risk |

**👉 Output:** Probability of disruption

## ⚙️ System Architecture

```
User
  ↓
Location API (IP-based)
  ↓
Weather API + AQI API
  ↓
ML Model (Risk Prediction)
  ↓
Streamlit Dashboard
```

## 📡 How It Works (Flow)

1. User opens the application
2. System detects location (IP-based or manual input)
3. Fetches:
   - Weather data 🌧️
   - AQI data 🌫️
4. ML model predicts risk score
5. UI displays:
   - Risk level
   - Environmental conditions
6. Live updates adjust risk dynamically

## 🧠 Technical Implementation

- **Frontend:** Streamlit
- **Backend:** Python
- **ML Model:** Logistic Regression (Scikit-learn)
- **APIs:** OpenWeather API, IP Geolocation API
- **Libraries:**
  - NumPy
  - Requests
  - Joblib
  - Pandas

## 📉 Market Crash Relevance 🚨

During economic downturns:

- Gig workers are the most affected
- Demand fluctuates unpredictably
- Income instability increases

### 💥 How Our Solution Helps

- Predicts low-demand / high-risk periods
- Enables workers to:
  - Avoid unprofitable hours
  - Optimize working time
- Supports future automated insurance payouts

**👉 Creates a financial safety layer for gig workers**

## 🔮 Future Enhancements

### 📸 Photo-Based Risk Detection

Users upload real-time images. AI detects:
- Rain intensity
- Road conditions
- Visibility

### 📍 Geo-Tagged Image Validation

Ensures:
- Location authenticity
- Fraud prevention

### 📈 Time-Series Prediction

Predicts risk for upcoming hours using:
- LSTM models
- Sequence-based forecasting

### 🔔 Alert System

"High risk expected in the next 2 hours"

### 💳 Parametric Insurance

Automatic payouts triggered by:
- Environmental thresholds
- No manual claim process required

## 🏆 Use Cases

- 🚴 Delivery platforms (Zomato, Swiggy)
- 👷 Gig worker protection systems
- 💼 Insurance technology (InsurTech)
- 🌆 Smart city monitoring

## 🚀 How to Run

```bash
# Clone the repository
git clone https://github.com/CodeStartAI-009/guidwire.git

# Navigate into the project directory
cd guidwire

# Create virtual environment
python3 -m venv venv

# Activate environment
source venv/bin/activate  # macOS/Linux
# venv\Scripts\activate   # Windows

# Install dependencies
pip install -r requirements.txt

# Set API key
export OPENWEATHER_API_KEY="your_api_key_here"

# Train the model
python ml/train_model.py

# Run the app
streamlit run app.py
```