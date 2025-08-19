import os
import pytest
import sqlite3
from storage.database import DatabaseManager

@pytest.fixture
def sample_data():
    return [
        {"id": "bitcoin", "symbol": "BTC", "name": "Bitcoin",
         "current_price": 101000, "market_cap": 510000000,
         "price_change_24h": 3.0, "volume": 11000000},
        {"id": "ethereum", "symbol": "ETH", "name": "Ethereum",
         "current_price": 3900, "market_cap": 195000000,
         "price_change_24h": -2.0, "volume": 4800000},
    ]

@pytest.fixture
def db(tmp_path):
    """Use a temporary DB file for testing"""
    db_file = tmp_path / "test_crypto.db"
    db_manager = DatabaseManager(db_file)
    yield db_manager
    db_manager.close()

def test_insert_and_fetch(db, sample_data):
    # Insert sample rows
    db.insert_data(sample_data)

    # Fetch all rows back
    rows = db.fetch_all()

    # Ensure correct number of rows
    assert len(rows) == 2

    # Verify content
    btc = next(r for r in rows if r["symbol"] == "BTC")
    eth = next(r for r in rows if r["symbol"] == "ETH")

    assert btc["name"] == "Bitcoin"
    assert btc["current_price"] == 101000
    assert eth["market_cap"] == 195000000
    assert isinstance(btc["volume"], int)
