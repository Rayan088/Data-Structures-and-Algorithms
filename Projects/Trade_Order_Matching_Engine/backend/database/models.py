from backend.database.db import db

class Wallet(db.Model):
    __tablename__ = "wallets"

    wallet_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)

    btc_balance = db.Column(db.Float, default=1.0)
    usd_balance = db.Column(db.Float, default=0.0)

# Creating Wallet table

class Order(db.Model):
    __tablename__ = "orders"

    order_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    side = db.Column(db.String(10), nullable=False)
    price = db.Column(db.Float, nullable=False)
    quantity = db.Column(db.Float, nullable=False)
    filled = db.Column(db.Float, default=0)
    status = db.Column(db.String(10), default="OPEN")
    time = db.Column(db.Float)

# Creating user order table