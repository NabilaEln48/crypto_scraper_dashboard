# report/charts.py
import plotly.graph_objects as go
import pandas as pd

def plot_candlestick_chart(df, coin_symbol):
    """
    Plot realistic candlestick + volume chart for a coin.
    """
    coin_data = df[df["symbol"] == coin_symbol.upper()].copy()
    if coin_data.empty:
        return None

    coin_data["timestamp"] = pd.to_datetime(coin_data["timestamp"])

    fig = go.Figure()

    fig.add_trace(go.Candlestick(
        x=coin_data["timestamp"],
        open=coin_data["price"],
        high=coin_data["price"] * (1 + coin_data["change_24h"] / 100),
        low=coin_data["price"] * (1 - abs(coin_data["change_24h"]) / 100),
        close=coin_data["price"],
        name=coin_symbol.upper()
    ))

    fig.add_trace(go.Bar(
        x=coin_data["timestamp"],
        y=coin_data["volume"],
        name="Volume",
        marker=dict(color="rgba(0, 100, 200, 0.3)"),
        yaxis="y2"
    ))

    fig.update_layout(
        title=f"{coin_symbol.upper()} Real-Time Price Trend",
        xaxis=dict(title="Time", rangeslider=dict(visible=False)),
        yaxis=dict(title="Price (USD)"),
        yaxis2=dict(title="Volume", overlaying="y", side="right"),
        template="plotly_dark",
        legend=dict(orientation="h")
    )

    return fig
