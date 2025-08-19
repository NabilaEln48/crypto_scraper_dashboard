# dashboard.py
import streamlit as st
from storage.database import Database
from report.report_generator import ReportGenerator
from report.charts import plot_candlestick_chart

# Page config
st.set_page_config(page_title="Crypto Dashboard", layout="wide")

st.title("📊 Crypto Dashboard")

# ========= Load Data =========
db = Database()
df = db.to_dataframe()

if df is None or df.empty:
    st.warning("⚠️ No data available. Run main.py first to scrape crypto prices.")
else:
    # Sidebar
    st.sidebar.header("Controls")
    coin_list = df["symbol"].unique().tolist()
    selected_coin = st.sidebar.selectbox("Select Coin", coin_list)

    # Report Summary
    report = ReportGenerator(df)

    st.subheader("📌 Latest Prices")
    st.dataframe(report.summary_by_latest())

    gainers, losers = report.top_gainers_losers()
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("🚀 Top Gainers")
        st.dataframe(gainers)

    with col2:
        st.subheader("📉 Top Losers")
        st.dataframe(losers)

    # Chart Section
    st.subheader(f"📈 {selected_coin} Price Trend (Candlestick)")
    fig = plot_candlestick_chart(df, selected_coin)
    if fig:
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.warning(f"No data found for {selected_coin}")
