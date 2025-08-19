# utils/helpers.py
import datetime

def get_timestamp():
    """
    Return the current timestamp as a string.
    Format: YYYY-MM-DD HH:MM:SS
    """
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def format_price(value):
    """
    Format numbers into a readable price string.
    Example: 12345.678 -> '12,345.68'
    """
    try:
        return f"${value:,.2f}"
    except (TypeError, ValueError):
        return "N/A"


def format_percentage(value):
    """
    Format float into percentage string with 2 decimals.
    Example: -0.2345 -> '-0.23%'
    """
    try:
        return f"{value:.2f}%"
    except (TypeError, ValueError):
        return "N/A"


def safe_get(d: dict, key: str, default=None):
    """
    Safely get a value from a dictionary with a default fallback.
    """
    return d.get(key, default)
