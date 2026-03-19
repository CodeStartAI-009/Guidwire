import numpy as np
import joblib
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report


# -------------------------------
# CREATE / LOAD DATASET
# -------------------------------
def generate_dataset():
    """
    Generate synthetic dataset for training

    Features:
        rain (0–100 mm)
        AQI (1–5)

    Label:
        0 = safe
        1 = risky
    """

    np.random.seed(42)

    rain = np.random.uniform(0, 100, 500)
    aqi = np.random.randint(1, 6, 500)

    X = np.column_stack((rain, aqi))

    # Define risk logic (more realistic)
    y = []

    for r, a in zip(rain, aqi):
        if r > 30 or a >= 4:
            y.append(1)  # risky
        else:
            y.append(0)  # safe

    return X, np.array(y)


# -------------------------------
# TRAIN MODEL
# -------------------------------
def train():
    X, y = generate_dataset()

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = LogisticRegression()
    model.fit(X_train, y_train)

    # Evaluation
    y_pred = model.predict(X_test)

    print("✅ Accuracy:", accuracy_score(y_test, y_pred))
    print("\n📊 Classification Report:\n", classification_report(y_test, y_pred))

    return model


# -------------------------------
# SAVE MODEL
# -------------------------------
def save_model(model, path="ml/risk_model.pkl"):
    joblib.dump(model, path)
    print(f"💾 Model saved at {path}")


# -------------------------------
# MAIN
# -------------------------------
if __name__ == "__main__":
    model = train()
    save_model(model)