import pytest
from scraper.api_scraper import APIScraper

def test_api_scraper_fetch_and_parse():
    scraper = APIScraper(coins=["bitcoin", "ethereum"])
    raw_data = scraper.fetch_data()
    
    # Check API returns data
    assert isinstance(raw_data, list)
    assert len(raw_data) > 0
    
    parsed = scraper.parse_data(raw_data)
    
    # Validate parsed structure
    assert isinstance(parsed, list)
    assert "symbol" in parsed[0]
    assert "current_price" in parsed[0]
