# scraper/api_scraper.py
import requests
from scraper.base_scraper import BaseScraper
from utils.logger import logger  

class APIScraper(BaseScraper):
    """
    CoinGecko API Scraper
    Fetches crypto data via API and parses JSON.
    """

    def __init__(self, vs_currency="usd", coins=None):
        super().__init__("CoinGeckoAPI")
        self.vs_currency = vs_currency
        self.coins = coins or ["bitcoin", "ethereum", "solana"]
        self.url = "https://api.coingecko.com/api/v3/coins/markets"

    def fetch_data(self, **kwargs):
        params = {
            "vs_currency": self.vs_currency,
            "ids": ",".join(self.coins),
            "order": "market_cap_desc",
            "per_page": len(self.coins),
            "page": 1,
            "sparkline": False
        }
        logger.info(f"Fetching data for coins={self.coins} in {self.vs_currency.upper()}...")
        try:
            response = requests.get(self.url, params=params, timeout=10)
            response.raise_for_status()
            logger.info("✅ API data fetched successfully.")
            return response.json()
        except requests.exceptions.RequestException as e:
            logger.error(f"❌ API request failed: {e}", exc_info=True)
            return []

    def parse_data(self, raw_data):
        """Convert raw JSON to clean dict list"""
        parsed = []
        for coin in raw_data:
            parsed.append({
                "id": coin["id"],
                "symbol": coin["symbol"].upper(),
                "name": coin["name"],
                "price": coin["current_price"],  
                "market_cap": coin["market_cap"],
                "change_24h": coin["price_change_percentage_24h"],  
                "volume": coin["total_volume"]
            })
        logger.info(f"Parsed {len(parsed)} coins from API response.")
        return parsed
