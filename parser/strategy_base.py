# parser/strategy_base.py
from abc import ABC, abstractmethod

class ParserStrategy(ABC):
    """
    Abstract base class for parsing strategies.
    Defines the interface for all concrete parsers.
    """

    @abstractmethod
    def parse(self, raw_data):
        """
        Parse raw input data (JSON, HTML, XML, etc.)
        and return a normalized list of dicts.
        Each dict should have at least:
          - name
          - symbol
          - current_price
          - price_change_24h
          - market_cap
          - volume
        """
        pass
