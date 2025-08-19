from scraper.api_scraper import APIScraper
from scraper.html_scraper import HTMLScraper

class ScraperFactory:
    @staticmethod
    def get_scraper(scraper_type: str, **kwargs):
        if scraper_type == "api":
            return APIScraper(**kwargs)
        elif scraper_type == "html":
            return HTMLScraper(**kwargs)
        else:
            raise ValueError(f"Unknown scraper type: {scraper_type}")
