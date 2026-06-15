import requests

BASE_URL = "https://api.binance.com"

def get_btc_market_data():
    response = requests.get(
        BASE_URL + "/api/v3/ticker/24hr",
        params={"symbol":"BTCUSDT"}
    )

    data = response.json()

    return {
        "price": float(data["lastPrice"]),
        "change": float(data["priceChangePercent"]),
        "high": float(data["highPrice"]),
        "low": float(data["lowPrice"]),
        "volume": float(data["volume"])
    }

# Function to get market data