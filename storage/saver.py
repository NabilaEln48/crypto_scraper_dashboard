import csv
from datetime import datetime
from utils.logger import logger


class CSVSaver:
    """
    Save crypto data into CSV file.
    """

    def __init__(self, filename="crypto_data.csv"):
        self.filename = filename

    def save(self, data):
        """Save a list of coin dicts to CSV"""
        if not data:
            logger.warning("No data to save to CSV.")
            return

        fieldnames = ["timestamp", "name", "symbol", "price", "change_24h", "market_cap", "volume"]

        with open(self.filename, mode="a", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)

            # Write header only if file is empty
            if file.tell() == 0:
                writer.writeheader()

            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            for coin in data:
                writer.writerow({
                    "timestamp": timestamp,
                    "name": coin["name"],
                    "symbol": coin["symbol"],
                    "price": coin["price"],
                    "change_24h": coin["change_24h"],
                    "market_cap": coin["market_cap"],
                    "volume": coin.get("volume", None),
                })

        logger.info(f" Data saved to {self.filename}")
