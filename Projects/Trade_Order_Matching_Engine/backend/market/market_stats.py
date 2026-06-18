def calculate_market_stats(order_book):

    bids = order_book.get_bids()
    asks = order_book.get_asks()

    if not bids or not asks:
        return {
            "mean_bid": None,
            "mean_ask": None,
            "spread": None
        }

    bid_prices = [order.price for order in bids]
    ask_prices = [order.price for order in asks]

    mean_bid = sum(bid_prices) / len(bid_prices)
    mean_ask = sum(ask_prices) / len(ask_prices)
    mean_price = (mean_bid + mean_ask) / 2

    spread = mean_ask - mean_bid
    spread_percent = (spread / mean_price) * 100

    return {
        "mean_price": round(mean_price, 2),
        "spread": f"{round(spread, 2)} ({round(spread_percent, 2)}%)"
    }

# Method to calculate mean price and spread