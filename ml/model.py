import numpy as np
from sklearn.linear_model import LogisticRegression

# -------------------------------
# TRAIN MODEL (DUMMY DATA FOR DEMO)
# -------------------------------

# Features: [rain (mm), AQI (1–5)]
X = np.array([
    [0, 1],
    [2, 1],
    [5, 2],
    [10, 3],
    [20, 3],
    [30, 4],
    [50, 5],
    [70, 5],
])

# Labels: 0 = safe, 1 = risky
y = np.array([
    0,
    0,
    0,
    0,
    1,
    1,
    1,
    1,
])

# Train model
model = LogisticRegression()
model.fit(X, y)


# -------------------------------
# PREDICTION FUNCTION
# -------------------------------
def predict_risk(rain, aqi):
    """
    Predict risk score based on rain and AQI

    Args:
        rain (float): rainfall in mm
        aqi (int): AQI level (1–5)

    Returns:
        float: risk score (0–1)
    """

    # Input formatting
    input_data = np.array([[rain, aqi]])

    # Probability of "risky" class
    risk_score = model.predict_proba(input_data)[0][1]

    return float(risk_score)