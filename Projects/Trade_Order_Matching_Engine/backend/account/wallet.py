class Wallet:
    def __init__(self):
        self.btc = 1.0
        self.cash = 0.0

    def can_buy(self, cost):
        return self.cash >= cost
    
    # Method if user has funds to buy
    
    def can_sell(self, qty):
        return self.btc >= qty
    
    # Method if user has funds to sell

    def buy_btc(self, price, quantity):
        cost = price * quantity

        if self.cash >= cost:
            self.cash -= cost
            self.btc += quantity

            return True
        
        return False
    
    # Method calculating funds after purchase
    
    def sell_btc(self, price, quantity):
        if self.btc >= quantity:
            revenue = price * quantity

            self.btc -= quantity
            self.cash += revenue

            return True
        
        return False
    
    # Method calculating funds after sale

    def get_total_value(self, btc_price):
        return self.cash + (self.btc * btc_price)
    
    # Method calculating total portfolio value

    def get_balance(self):
        return {
            "BTC": self.btc,
            "USD": self.cash
        }
    
    # Method returning current balance