# storage/loader.py
import pandas as pd

class CSVLoader:
    """
    Loads crypto data from CSV into a Pandas DataFrame.
    """

    def __init__(self, filename="crypto_data.csv"):
        self.filename = filename

    def load(self):
        """Load CSV into DataFrame"""
        try:
            df = pd.read_csv(self.filename)
            return df
        except FileNotFoundError:
            print(" No CSV file found. Run the scraper first.")
            return None
