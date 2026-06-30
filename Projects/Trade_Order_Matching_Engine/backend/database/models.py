from backend.database.db import db

class Wallet(db.Model):
    __tablename__ = "wallets" # Table name

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)

    btc_balance = db.Column(db.Float, default=1.0)
    usd_balance = db.Column(db.Float, default=0.0)