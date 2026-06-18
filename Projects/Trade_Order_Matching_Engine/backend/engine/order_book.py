from .order import Order
import heapq

# OrderBook class

class OrderBook:
    def __init__(self):
        self.bids = []
        self.asks = []

        self.bid_display = []
        self.ask_display = []

    def add_order(self, order):
        if order.side == "BUY":
            heapq.heappush(self.bids, (-order.price, order.time, order))

            self.bid_display.append(order)
            self.sort_bid_display()
        
        elif order.side == "SELL":
            heapq.heappush(self.asks, (order.price, order.time, order))

            self.ask_display.append(order)
            self.sort_ask_display()
    
    # Method which adds and sorts orders based on side

    def sort_bid_display(self):
        self.bid_display.sort(key=lambda order: order.price, reverse=True)

    # Method to sort full bid list

    def sort_ask_display(self):
        self.ask_display.sort(key=lambda order: order.price)

    # Method to sort full asks list

    def get_best_bid(self):
        if self.bids:
            return self.bids[0][2]
        return None
    
    # Method which returns highest bid
    
    def get_best_ask(self):
        if self.asks:
            return self.asks[0][2]
        return None
    
    # Method which returns lowest sell 

    def remove_best_bid(self):
        if self.bids:
            heapq.heappop(self.bids)

    # Method which removes best bid

    def remove_best_ask(self):
        if self.asks:
            heapq.heappop(self.asks)

    # Method which removes best ask

    def get_order_book_display(self):
        return {
            "bids": [{"price": order.price,
                      "quantity": order.quantity}
                      
                      for order in self.bid_display],

            "asks": [{"price": order.price,
                      "quantity": order.quantity}
                      
                      for order in self.ask_display]
        }
    
    # Method to display all bids and asks