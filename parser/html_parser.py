# parser/html_parser.py
from bs4 import BeautifulSoup
from parser.strategy_base import ParserStrategy

class HTMLParserStrategy(ParserStrategy):
    """
    Concrete strategy to parse cryptocurrency data from raw HTML.
    """

    def parse(self, html_content):
        """
        Parse HTML and extract crypto data.
        Expected HTML structure must be adapted based on target site.
        """
        soup = BeautifulSoup(html_content, "html.parser")
        coins = []

        # Example: adapt this to the target website’s structure
        rows = soup.select("table tr")  # scraping rows in a table
        for row in rows[1:]:  # skip header
            cols = row.find_all("td")
            if len(cols) >= 3:
                coin = {
                    "name": cols[0].get_text(strip=True),
                    "symbol": cols[1].get_text(strip=True).upper(),
                    "current_price": self._safe_float(cols[2].get_text(strip=True)),
                }
                coins.append(coin)

        return coins

    def _safe_float(self, text):
        """Convert string to float safely (removes $ , and % signs)."""
        try:
            return float(text.replace(",", "").replace("$", "").replace("%", ""))
        except ValueError:
            return None
