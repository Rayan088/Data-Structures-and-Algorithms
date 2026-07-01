from .order_book import OrderBook
from .trade import Trade

# Matching Engine class

class MatchingEngine:
    def __init__(self, wallet):
        self.wallet = wallet
        self.order_book = OrderBook()
        self.trades = []
        self.user_orders = []

    def add_order(self, order):
        if order.is_user:
            self.user_orders.append(order)
            
        self.order_book.add_order(order)
        self.match_orders(order)

    # Method to add orders to orderbook

    def match_orders(self, incoming_order):
        try: 
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

                quantity = round(min(buy.quantity - buy.filled, sell.quantity- sell.filled), 8)

                # break if number is less that one hundred-milionth
                if quantity <= 1e-8:
                    break
                
                trade = Trade(buy, sell, sell.price, quantity)

                trade.taker_side = incoming_order.side

                self.trades.append(trade)

                if buy.is_user:
                    self.wallet.btc += trade.quantity
                    self.wallet.cash -= trade.quantity * trade.price

                if sell.is_user:
                    self.wallet.btc -= trade.quantity
                    self.wallet.cash += trade.quantity * trade.price

                buy.filled = round(buy.filled + quantity, 8)
                sell.filled = round(sell.filled + quantity, 8)

                if buy.filled >= buy.quantity:
                    buy.status = "CLOSED"
                    self.order_book.remove_best_bid()
                    self.order_book.remove_order_from_display(buy)
                
                if sell.filled >= sell.quantity:
                    sell.status = "CLOSED"
                    self.order_book.remove_best_ask()
                    self.order_book.remove_order_from_display(sell)

                if buy.status != "CLOSED" and sell.status != "CLOSED":
                    break

        except Exception as e:
            print(f"Match error: {e}")

    # Method to match orders