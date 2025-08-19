import os
import pandas as pd
import pytest
from storage.saver import CSVSaver
from storage.loader import CSVLoader

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

def test_csv_saver_and_loader(tmp_path, sample_data):
    # Path for temp CSV file
    file_path = tmp_path / "crypto_data.csv"

    # Save data
    saver = CSVSaver(filename=file_path)
    saver.save(sample_data)

    # Check file created
    assert file_path.exists()

    # Load back
    loader = CSVLoader(filename=file_path)
    df = loader.load()

    # Verify DataFrame content
    assert isinstance(df, pd.DataFrame)
    assert not df.empty
    assert "symbol" in df.columns
    assert df.loc[df["symbol"] == "BTC", "name"].values[0] == "Bitcoin"
    assert df.loc[df["symbol"] == "ETH", "current_price"].values[0] == 3900
