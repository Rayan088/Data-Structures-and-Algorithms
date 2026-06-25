from .binance_api import get_btc_market_data

def get_market_summary():
    data = get_btc_market_data()

    market = {
     "asset": "BTC",
     "current_price": data["price"],
     "change_24h": data["change"],
     "highlow": f"{data['high']} / {data['low']}",
     "volume": data["volume"]   
    }

    return market

# Function to get market summary