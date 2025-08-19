# scraper/base_scraper.py
from abc import ABC, abstractmethod

class BaseScraper(ABC):
    """
    Abstract base class for all scrapers.
    Defines the interface for fetching and parsing data.
    """

    def __init__(self, source_name: str):
        self.source_name = source_name

    @abstractmethod
    def fetch_data(self, **kwargs):
        """
        Fetch raw data from the source (API call, HTML request, etc.)
        Returns raw response.
        """
        pass

    @abstractmethod
    def parse_data(self, raw_data):
        """
        Parse raw response into structured Python objects (dicts, lists).
        Returns structured data ready for storage or reporting.
        """
        pass

    def run(self, **kwargs):
        """
        Template method: fetch → parse.
        All scrapers will use this common workflow.
        """
        raw = self.fetch_data(**kwargs)
        parsed = self.parse_data(raw)
        return parsed
