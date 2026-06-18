import time

# Class for successful trades

class Trade:
    trade_counter = 1

    def __init__(self, buy_order, sell_order, price, quantity):
        self.trade_id = Trade.trade_counter

        Trade.trade_counter += 1

        self.buy_order = buy_order
        self.sell_order = sell_order
        self.price = price
        self.quantity = quantity

        self.side = buy_order.side

        self.time = time.time()

    def get_trade_data(self):
        return {
            "trade_id": self.trade_id,
            "buy_order": self.buy_order,
            "sell_order": self.sell_order,
            "price": self.price,
            "quantity": self.quantity,
            "time": self.time
        }
    
    # Method returning trade data in a string