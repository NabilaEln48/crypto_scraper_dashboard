import pytest
from parser.json_parser import JSONParser

def test_json_parser_extracts_data():
    # Fake API-like JSON from CoinGecko
    fake_json = [
        {
            "id": "bitcoin",
            "symbol": "btc",
            "name": "Bitcoin",
            "current_price": 100000,
            "market_cap": 500000000,
            "price_change_percentage_24h": 3.5,
            "total_volume": 10000000
        },
        {
            "id": "ethereum",
            "symbol": "eth",
            "name": "Ethereum",
            "current_price": 4000,
            "market_cap": 200000000,
            "price_change_percentage_24h": -1.2,
            "total_volume": 5000000
        }
    ]

    parser = JSONParser()
    result = parser.parse(fake_json)

    # Ensure result is a list of dicts
    assert isinstance(result, list)
    assert len(result) == 2

    # Validate Bitcoin
    btc = result[0]
    assert btc["name"] == "Bitcoin"
    assert btc["symbol"] == "BTC"
    assert btc["current_price"] == 100000
    assert btc["price_change_24h"] == 3.5

    # Validate Ethereum
    eth = result[1]
    assert eth["symbol"] == "ETH"
    assert eth["price_change_24h"] == -1.2
