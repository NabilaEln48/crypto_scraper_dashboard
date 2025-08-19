# utils/logger.py
import logging
import os

# Create logs directory if not exists
if not os.path.exists("logs"):
    os.makedirs("logs")

# Configure logger
logging.basicConfig(
    level=logging.INFO,   # DEBUG, INFO, WARNING, ERROR, CRITICAL
    format="%(asctime)s [%(levelname)s] %(name)s - %(message)s",
    handlers=[
        logging.FileHandler("logs/app.log", encoding="utf-8"),
        logging.StreamHandler()  # also prints to console
    ]
)

# Global logger
logger = logging.getLogger("CryptoScraper")
