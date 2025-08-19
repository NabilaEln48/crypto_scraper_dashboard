# parser/json_parser.py
from parser.strategy_base import ParserStrategy

class JSONParserStrategy(ParserStrategy):
    """
    Concrete strategy to parse cryptocurrency data from JSON response.
    """

    def parse(self, json_data):
        """
        Parse JSON and normalize into a list of coin dicts.
        Expected structure matches CoinGecko API.
        """
        coins = []

        for entry in json_data:
            coin = {
                "name": entry.get("name"),
                "symbol": entry.get("symbol", "").upper(),
                "current_price": entry.get("current_price"),
                "price_change_24h": entry.get("price_change_percentage_24h"),
                "market_cap": entry.get("market_cap"),
                "volume": entry.get("total_volume"),
            }
            coins.append(coin)

        return coins
