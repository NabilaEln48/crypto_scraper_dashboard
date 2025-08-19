# 📊 Crypto Scraper Dashboard

A modular Python project that scrapes live cryptocurrency data from the **CoinGecko API**, stores it in **SQLite + CSV**, and visualizes insights in an **interactive Streamlit dashboard**.  

This project follows **Software Engineering principles** with **design patterns** for scalability and maintainability.

---

##  Features
-  **Scraping Layer** – Fetches live data from CoinGecko API.
-  **Storage Layer** – Saves to **SQLite DB** (`crypto_data.db`) and **CSV** (`crypto_data.csv`).
-  **Reporting Layer** – Generates summaries (latest prices, gainers, losers).
-  **Dashboard Layer** – Interactive **Streamlit app** with tables + charts.
-  **Charts** – Realistic candlestick charts with **volume overlay** (Plotly).
-  **Design Patterns** applied for clean architecture.

---

##  Architecture & Design Patterns

### 1. **Scraper Layer**
- **BaseScraper (Abstract Class / Template Method)**  
  Defines a common interface for scrapers (`fetch_data`, `parse_data`).
- **APIScraper (Concrete Implementation)**  
  Implements API-specific fetching & parsing.  

 **Pattern Used**: **Template Method** – ensures consistent data flow (`fetch → parse`).

---

### 2. **Storage Layer**
- **Database (Singleton)**  
  Only one database connection is active throughout the app.  
  ```python
  db1 = Database()
  db2 = Database()
  assert db1 is db2  #  Same instance**

  CSVLoader / Saver
Handles persistence to CSV files.

 Pattern Used: Singleton for DB, DAO (Data Access Object) for persistence abstraction.

3. Report Layer

ReportGenerator
Provides high-level summaries:

Latest prices

Top gainers & losers

Export to CSV

 Pattern Used: Strategy (Analysis Methods) – multiple report generation strategies (summary, gainers, losers).

4. Dashboard Layer

Streamlit UI
Provides data exploration via:

Sidebar coin selector

Tables for gainers/losers

Interactive price trend chart

 Pattern Used: MVC (Model-View-Controller)

Model → Database (SQLite)

View → Streamlit Dashboard

Controller → ReportGenerator + Charts

5. Utilities

Logger (Singleton / Wrapper)
Unified logging across modules.


# Future Enhancements

 Real-time auto-refresh in dashboard

 Push notifications for price alerts

 Technical indicators (SMA, EMA, RSI, MACD)

 Multi-currency support (USD, EUR, CAD, etc.)

