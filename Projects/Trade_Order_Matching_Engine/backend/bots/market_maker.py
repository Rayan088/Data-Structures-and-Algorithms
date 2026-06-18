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

        spread = random.randint(10, 100)
        quantity = round(random.uniform(0.01, 0.5), 3)

        buy_order = Order("BUY", current_price - spread, quantity)
        sell_order = Order("SELL", current_price + spread, quantity)

        return buy_order, sell_order
    
    # Method to create order
    
    def start(self):
        self.running = True

        while self.running:
            buy, sell = self.create_order()

            self.engine.add_order(buy)
            self.engine.add_order(sell)

            time.sleep(5)

    # Method to add bot orders to bid and asks lists

    def stop(self):
        self.running = False

    # Method to stop from running