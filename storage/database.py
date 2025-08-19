import sqlite3
import pandas as pd
from datetime import datetime

class Database:
    """
    Singleton Database class for SQLite storage of crypto data.
    """

    _instance = None

    def __new__(cls, db_name="crypto_data.db"):
        if cls._instance is None:
            cls._instance = super(Database, cls).__new__(cls)
            cls._instance.db_name = db_name
            cls._instance.conn = sqlite3.connect(db_name, check_same_thread=False)
            cls._instance.cursor = cls._instance.conn.cursor()
            cls._instance._create_table()
        return cls._instance

    def _create_table(self):
        """Create table if not exists"""
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS crypto_data (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp TEXT,
                name TEXT,
                symbol TEXT,
                price REAL,
                change_24h REAL,
                market_cap REAL,
                volume REAL
            )
        """)
        self.conn.commit()

    def reset_table(self):
        """Drop and recreate table (useful if schema changes)"""
        self.cursor.execute("DROP TABLE IF EXISTS crypto_data")
        self.conn.commit()
        self._create_table()

    def insert_data(self, data):
        """Insert list of coin dictionaries into DB"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        for coin in data:
            self.cursor.execute("""
                INSERT INTO crypto_data (timestamp, name, symbol, price, change_24h, market_cap, volume)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            """, (
                timestamp,
                coin["name"],
                coin["symbol"],
                coin["price"],
                coin["change_24h"],
                coin["market_cap"],
                coin.get("volume", None)
            ))
        self.conn.commit()

    def fetch_latest(self):
        """Fetch latest entry for each coin (as list of tuples)"""
        query = """
        SELECT * FROM crypto_data
        WHERE rowid IN (
            SELECT MAX(rowid) 
            FROM crypto_data
            GROUP BY symbol
        )
        """
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def fetch_all(self, symbol=None):
        """Fetch all rows, optionally filter by symbol"""
        if symbol:
            self.cursor.execute("SELECT * FROM crypto_data WHERE symbol = ? ORDER BY timestamp", (symbol.upper(),))
        else:
            self.cursor.execute("SELECT * FROM crypto_data ORDER BY timestamp")
        return self.cursor.fetchall()

    def to_dataframe(self, symbol=None):
        """Return data as pandas DataFrame"""
        query = "SELECT * FROM crypto_data"
        if symbol:
            query += f" WHERE symbol='{symbol.upper()}'"
        return pd.read_sql_query(query, self.conn)

    def close(self):
        """Close connection"""
        self.conn.close()
