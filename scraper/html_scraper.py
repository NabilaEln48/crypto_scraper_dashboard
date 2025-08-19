# scraper/html_scraper.py
import requests
from bs4 import BeautifulSoup
from scraper.base_scraper import BaseScraper

class HTMLScraper(BaseScraper):
    """
    CoinMarketCap HTML Scraper
    Scrapes crypto data from the web page using BeautifulSoup.
    """

    def __init__(self, url="https://coinmarketcap.com/"):
        super().__init__("CoinMarketCapHTML")
        self.url = url

    def fetch_data(self, **kwargs):
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                          "AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/120.0.0.0 Safari/537.36"
        }
        response = requests.get(self.url, headers=headers)
        response.raise_for_status()
        return response.text

    def parse_data(self, raw_data):
        """
        Extract top cryptos (name, symbol, price, 24h % change, market cap).
        """
        soup = BeautifulSoup(raw_data, "html.parser")
        table = soup.find("table")   # main crypto table
        rows = table.find("tbody").find_all("tr")

        parsed = []
        for row in rows[:10]:  # limit to top 10 for now
            cols = row.find_all("td")

            try:
                name = cols[2].find("p", class_="kKpPOn").text  # Coin name
                symbol = cols[2].find("p", class_="coin-item-symbol").text
                price = cols[3].text.replace("$", "").replace(",", "")
                change_24h = cols[4].text.replace("%", "").replace(",", "")
                market_cap = cols[7].text.replace("$", "").replace(",", "")

                parsed.append({
                    "name": name,
                    "symbol": symbol,
                    "current_price": float(price),
                    "price_change_24h": float(change_24h),
                    "market_cap": market_cap
                })
            except Exception:
                continue  # skip malformed rows

        return parsed
