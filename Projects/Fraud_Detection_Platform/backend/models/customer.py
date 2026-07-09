from database.db import db

class Customer(db.Model):
    __tablename__ = "customers"

    customer_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    account_type = db.Column(db.String(40), nullable=False)
    account_status = db.Column(db.String(20), default="ACTIVE")
    risk_score = db.Column(db.Integer, default=0)
    home_country = db.Column(db.String(30))
