def risk_label(score):
    """
    Convert risk score into label

    Args:
        score (float): 0–1

    Returns:
        str: LOW / MEDIUM / HIGH
    """

    if score >= 0.7:
        return "HIGH"
    elif score >= 0.4:
        return "MEDIUM"
    else:
        return "LOW"


def risk_color(score):
    """
    Return color based on risk level (for UI)

    Returns:
        str: 'green', 'orange', 'red'
    """

    if score >= 0.7:
        return "red"
    elif score >= 0.4:
        return "orange"
    else:
        return "green"


def format_aqi(aqi):
    """
    Convert AQI numeric value to readable text
    """

    mapping = {
        1: "Good",
        2: "Fair",
        3: "Moderate",
        4: "Poor",
        5: "Very Poor",
    }

    return mapping.get(aqi, "Unknown")


def safe_float(value, default=0.0):
    """
    Safely convert value to float
    """

    try:
        return float(value)
    except (TypeError, ValueError):
        return default