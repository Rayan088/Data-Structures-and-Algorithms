from .order_book import OrderBook
from .trade import Trade

# Matching Engine class

class MatchingEngine:
    def __init__(self, wallet):
        self.wallet = wallet
        self.order_book = OrderBook()
        self.trades = []

    def add_order(self, order):
        self.order_book.add_order(order)
        self.match_orders(order)

    # Method to add orders to orderbook

    def match_orders(self, incoming_order):
        while True:

            while self.order_book.bids:
                bid = self.order_book.get_best_bid()

                if bid.status == "CLOSED":
                    self.order_book.remove_best_bid()
                else:
                    break

            while self.order_book.asks:
                ask = self.order_book.get_best_ask()

                if ask.status == "CLOSED":
                    self.order_book.remove_best_ask()
                else:
                    break

            # Remove closed buy and sell orders

            buy = self.order_book.get_best_bid()
            sell = self.order_book.get_best_ask()

            if buy is None or sell is None:
                break

            if buy.price < sell.price:
                break

            quantity = min(buy.quantity - buy.filled, sell.quantity- sell.filled)

            if quantity <= 0:
                break
            
            trade = Trade(buy, sell, sell.price, quantity)

            trade.taker_side = incoming_order.side

            self.trades.append(trade)

            if buy.is_user:
                self.wallet.btc += trade.quantity
                self.wallet.usd -= trade.quantity * trade.price

            if sell.is_user:
                self.wallet.btc -= trade.quantity
                self.wallet.usd += trade.quantity * trade.price

            buy.filled += quantity
            sell.filled += quantity

            if buy.filled >= buy.quantity:
                buy.status = "CLOSED"
                self.order_book.remove_best_bid()
            
            if sell.filled >= sell.quantity:
                sell.status = "CLOSED"
                self.order_book.remove_best_ask()

    # Method to match orders