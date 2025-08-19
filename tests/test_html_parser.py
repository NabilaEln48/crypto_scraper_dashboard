import pytest
from parser.html_parser import HTMLParser

def test_html_parser_extracts_data():
    # Fake HTML snippet (simulating a table of crypto data)
    fake_html = """
    <html>
        <body>
            <table>
                <tr><td>Bitcoin</td><td>BTC</td><td>100000</td><td>500000000</td><td>+3.5%</td><td>10000000</td></tr>
                <tr><td>Ethereum</td><td>ETH</td><td>4000</td><td>200000000</td><td>-1.2%</td><td>5000000</td></tr>
            </table>
        </body>
    </html>
    """

    parser = HTMLParser()
    result = parser.parse(fake_html)

    # Ensure result is a list of dicts
    assert isinstance(result, list)
    assert len(result) == 2

    # Check structure
    btc = result[0]
    assert btc["name"] == "Bitcoin"
    assert btc["symbol"] == "BTC"
    assert isinstance(btc["current_price"], (int, float))

    eth = result[1]
    assert eth["symbol"] == "ETH"
    assert eth["price_change_24h"] == -1.2
