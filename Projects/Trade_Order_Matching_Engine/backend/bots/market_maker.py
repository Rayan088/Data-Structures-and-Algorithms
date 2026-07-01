import time
import random

from backend.engine.order import Order
from backend.market.market_data import get_market_summary

class MarketMaker:
    def __init__(self, engine):
        self.engine = engine
        self.running = False

    def create_order(self):
        market = get_market_summary()
        current_price = market["current_price"]

        buy_spread = round(current_price * random.uniform(0.0001, 0.0003), 2)
        sell_spread = round(current_price * random.uniform(0.0002, 0.0004), 2)
        quantity = round(random.uniform(0.01, 1.0), 3)

        buy_order = Order("BUY", current_price - buy_spread, quantity, is_user=False)
        sell_order = Order("SELL", current_price + sell_spread, quantity, is_user=False)

        return buy_order, sell_order
    
    # Method to create order
    
    def start(self):
        self.running = True

        while self.running:
            buy, sell = self.create_order()

            self.engine.add_order(buy)
            self.engine.add_order(sell)

            time.sleep(2)

    # Method to add bot orders to bid and asks lists

    def stop(self):
        self.running = False

    # Method to stop from running