from sqlalchemy import func

from database.db import db
from models.customer import Customer
from models.transactions import Transaction
from models.alert import Alert

class AnalyticsEngine:
    def total_transactions(self):
        return Transaction.query.count()

    # Method for total number of transactions

    def high_risk_alerts(self):
        return Transaction.query.filter(
            Transaction.risk_level.in_(["HIGH", "CRITICAL"])
        ).count()

    # Method for total number of high risk alerts

    def transactions_awaiting_review(self):
        return Transaction.query.filter_by(status="REVIEW").count()

    # Method for total number of pending transactions

    def fraud_prevented(self):
        total = (db.session.query(func.sum(Transaction.amount))
                .filter(Transaction.status == "BLOCKED").scalar())
        
        return total or 0

    # Method for total sum of fraud prevented

    def transactions_by_risk(self):
        results = (db.session.query(Transaction.risk_level, func.count())
                .group_by(Transaction.risk_level).all())
        
        return results

    # Method for count of transactions by risk level

    def riskiest_customers(self):
        return (Customer.query.order_by(Customer.risk_score.desc())
                .limit(5).all())

    # Method for top 5 highest risk scores

    def transactions_by_country(self):
        results = (db.session.query(Transaction.country, func.count())
                .group_by(Transaction.country).all())
        
        return results

    # Method for count of transactions by country

    def fraud_by_rule(self):
        fraud_by_rule = {
            "New Device": 0,
            "High Amount": 0,
            "Impossible Travel": 0,
            "Unfamiliar Merchant": 0
        }

        alerts = Alert.query.all()

        for alert in alerts:
            rules = alert.reasons.split(", ")
            for rule in rules:
                fraud_by_rule[rule] += 1

        return fraud_by_rule

    # Method for count of blocked accounts by restriction broken