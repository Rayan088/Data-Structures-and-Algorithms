from order import Order
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
            heapq.heappush(self.bids, (-order.price, order))

            self.bid_display.append(order)
            self.sort_bid_display()
        
        elif order.side == "SELL":
            heapq.heappush(self.asks, (order.price, order))

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
        if len(self.bids) > 0:
            return self.bids[0][1]
        return None
    
    # Method which returns highest bid
    
    def get_best_ask(self):
        if len(self.asks) > 0:
            return self.asks[0][1]
        return None
    
    # Method which returns lowest sell 

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