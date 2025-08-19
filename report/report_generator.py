import pandas as pd
from utils.logger import logger

class ReportGenerator:
    def __init__(self, df: pd.DataFrame):
        self.df = df

    def summary_by_latest(self):
        """Get the latest entry per coin"""
        latest = self.df.sort_values("timestamp").groupby("symbol").tail(1)
        # ✅ match DB column name exactly: change_24h
        return latest[["timestamp", "name", "symbol", "price", "change_24h", "market_cap", "volume"]]

    def top_gainers_losers(self, n=3):
        """Top gainers and losers based on 24h change"""
        latest = self.df.sort_values("timestamp").groupby("symbol").tail(1)
        top_gainers = latest.nlargest(n, "change_24h")
        top_losers = latest.nsmallest(n, "change_24h")
        return top_gainers, top_losers

    def export_csv(self, filename="crypto_report.csv"):
        """Export full DataFrame to CSV"""
        self.df.to_csv(filename, index=False)
        logger.info(f"📊 Report exported to {filename}")
