from scraper.factory import ScraperFactory
from storage.saver import CSVSaver
from storage.database import Database
from report.charts import plot_price_trend
from report.report_generator import ReportGenerator


def main():
    # ========= User Input =========
    user_input = input("Enter coins (comma separated, e.g., bitcoin,ethereum,solana) or press Enter for defaults: ")
    if user_input.strip():
        coins = [c.strip().lower() for c in user_input.split(",")]
    else:
        coins = ["bitcoin", "ethereum", "solana"]  # default

    # ========= Choose Scraper =========
    scraper = ScraperFactory.get_scraper("api", vs_currency="usd", coins=coins)

    # ========= Run Scraper =========
    data = scraper.run()

    # ========= Validate =========
    if not data:
        print(" No valid coin data found. Please check your input (e.g., 'dogecoin' not 'dodgecoin').")
        return

    # ========= Print Results =========
    print(f"\n=== Live Crypto Data from {scraper.source_name} ===")
    for coin in data:
        print(f"{coin['name']} ({coin['symbol']}): ${coin['price']:,} "
              f"(24h: {coin['change_24h']}%)")

    # ========= Save Results =========
    saver = CSVSaver()
    saver.save(data)

    db = Database()
    db.insert_data(data)
    print(" Data also saved to SQLite (crypto_data.db)")

    # ========= Load Data Back (from SQLite, not CSV) =========
    df = db.to_dataframe()
    if not df.empty:
        # --- Summary Report ---
        report = ReportGenerator(df)

        print("\n=== Latest Prices ===")
        print(report.summary_by_latest())

        gainers, losers = report.top_gainers_losers()
        print("\n=== Top Gainers ===")
        print(gainers)
        print("\n=== Top Losers ===")
        print(losers)

        report.export_csv("crypto_report.csv")  # still exportable

        # --- Chart ---
        coin_choice = input("\nEnter a coin symbol to see its price trend chart (e.g., BTC, ETH, SOL): ")
        if coin_choice.strip():
            plot_price_trend(df, coin_choice)


if __name__ == "__main__":
    main()
