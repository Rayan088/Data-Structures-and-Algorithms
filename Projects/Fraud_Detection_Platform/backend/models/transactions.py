from database.db import db

class Transaction(db.Model):
    __tablename__ = "transactions"

    transaction_id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey("customers.customer_id"), nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False)
    merchant = db.Column(db.String(100), nullable=False)
    amount = db.Column(db.Float(10, 2), nullable=False)
    currency = db.Column(db.String(10), default="GBP")
    country = db.Column(db.String(30), nullable=False)
    device = db.Column(db.String(50), nullable=False)
    risk_score = db.Column(db.Integer, default=0)
    risk_level = db.Column(db.String(20), default="LOW")
    status = db.Column(db.String(20), default="PENDING")
    analyst_action = db.Column(db.String(50), default=None)

    alert = db.relationship("Alert", backref="transaction", uselist=False)