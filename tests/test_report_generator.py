import pytest
import pandas as pd
from report.report_generator import ReportGenerator

@pytest.fixture
def sample_df():
    data = [
        {"timestamp": "2025-08-19 12:00:00", "name": "Bitcoin", "symbol": "BTC",
         "price": 100000, "24h_change": 2.5, "market_cap": 500000000, "volume": 10000000},
        {"timestamp": "2025-08-19 12:00:00", "name": "Ethereum", "symbol": "ETH",
         "price": 4000, "24h_change": -1.2, "market_cap": 200000000, "volume": 5000000},
        {"timestamp": "2025-08-19 13:00:00", "name": "Bitcoin", "symbol": "BTC",
         "price": 101000, "24h_change": 3.0, "market_cap": 510000000, "volume": 11000000},
        {"timestamp": "2025-08-19 13:00:00", "name": "Ethereum", "symbol": "ETH",
         "price": 3900, "24h_change": -2.0, "market_cap": 195000000, "volume": 4800000},
    ]
    return pd.DataFrame(data)

def test_summary_by_latest(sample_df):
    report = ReportGenerator(sample_df)
    latest = report.summary_by_latest()

    # Should return latest entry for BTC and ETH
    assert len(latest) == 2
    assert "BTC" in latest["symbol"].values
    assert "ETH" in latest["symbol"].values
    assert latest.loc[latest["symbol"] == "BTC", "price"].values[0] == 101000

def test_top_gainers_losers(sample_df):
    report = ReportGenerator(sample_df)
    gainers, losers = report.top_gainers_losers(n=1)

    # Top gainer should be BTC (3.0%)
    assert gainers.iloc[0]["symbol"] == "BTC"
    # Top loser should be ETH (-2.0%)
    assert losers.iloc[0]["symbol"] == "ETH"

def test_export_csv(tmp_path, sample_df):
    report = ReportGenerator(sample_df)
    file_path = tmp_path / "crypto_report.csv"

    report.export_csv(file_path)
    assert file_path.exists()

    # Load it back and check columns
    df = pd.read_csv(file_path)
    assert "symbol" in df.columns
    assert "price" in df.columns
