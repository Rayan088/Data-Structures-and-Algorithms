from database.db import db

class Alert(db.Model):
    __tablename__ = "alerts"

    alert_id = db.Column(db.Integer, primary_key=True)
    transaction_id = db.Column(db.Integer, db.ForeignKey("transactions.transaction_id"), nullable=False)
    customer_id = db.Column(db.Integer, db.ForeignKey("customers.customer_id"), nullable=False)
    risk_score = db.Column(db.Integer, nullable=False)
    reasons = db.Column(db.JSON)
    status = db.Column(db.String(20), default="PENDING")