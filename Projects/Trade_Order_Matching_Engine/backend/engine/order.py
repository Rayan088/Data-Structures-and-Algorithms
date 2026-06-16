import time

# Order class

class Order:
    order_id = 100

    def __init__(self, side, price, quantity):
        self.id = Order.order_id
        Order.order_id += 1

        self.time = time.time()

        self.side = side
        self.price = price
        self.quantity = quantity

        self.filled = 0
        self.status = "OPEN"


    def remaining_quantity(self):
        return self.quantity - self.filled
    
    # Method for remaining orders to be fulfilled