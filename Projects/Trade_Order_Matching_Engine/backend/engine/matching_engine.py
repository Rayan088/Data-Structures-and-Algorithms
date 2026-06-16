from order_book import OrderBook
from trade import Trade

# Matching Engine class

class MatchingEngine:
    def __init__(self):
        self.order_book = OrderBook()
        self.trades = []

    def add_order(self, order):
        self.order_book.add_order(order)
        self.match_orders()

    # Method to add orders to orderbook

    def match_orders(self):
        pass