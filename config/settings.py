# settings.py

"""
Global project settings and configuration.
Keeps constants and environment setup in one place.
"""

import os

# ========= General =========
APP_NAME = "Crypto Scraper Dashboard"
VERSION = "1.0.0"

# ========= API =========
COINGECKO_API_URL = "https://api.coingecko.com/api/v3/coins/markets"
DEFAULT_COINS = ["bitcoin", "ethereum", "solana"]
VS_CURRENCY = "usd"

# ========= Storage =========
DATA_DIR = os.path.join(os.getcwd(), "data")
CSV_FILE = os.path.join(DATA_DIR, "crypto_data.csv")
REPORT_FILE = os.path.join(DATA_DIR, "crypto_report.csv")
DB_FILE = os.path.join(DATA_DIR, "crypto_data.db")

# ========= Dashboard =========
DASHBOARD_TITLE = "📊 Crypto Dashboard"
DASHBOARD_REFRESH_SECONDS = 60   # auto-refresh interval

# ========= Logging =========
LOG_DIR = os.path.join(os.getcwd(), "logs")
LOG_FILE = os.path.join(LOG_DIR, "app.log")
LOG_LEVEL = "INFO"   # DEBUG, INFO, WARNING, ERROR, CRITICAL

# ========= Ensure directories exist =========
os.makedirs(DATA_DIR, exist_ok=True)
os.makedirs(LOG_DIR, exist_ok=True)
