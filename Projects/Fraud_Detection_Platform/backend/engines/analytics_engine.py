from sqlalchemy import func

from database.db import db
from models.customer import Customer
from models.transactions import Transaction

def total_transactions():
    return Transaction.query.count()

# Function for total number of transactions

def high_risk_alerts():
    return Transaction.query.filter(
        Transaction.risk_level.in_(["HIGH, CRITICAL"])
    ).count()

# Function for total number of high risk alerts

def transactions_awaiting_review():
    return Transaction.query.filter_by(status="PENDING").count()

# Function for total number of pending transactions

def fraud_prevented():
    total = (db.session.query(func.sum(Transaction.amount))
             .filter(Transaction.status == "BLOCKED").scalar())
    
    return total or 0

# Function for total sum of fraud prevented

def transactions_by_risk():
    results = (db.session.query(Transaction.risk_level, func.count())
               .group_by(Transaction.risk_level).all())
    
    return results

# Function for count of transactions by risk level

def riskiest_customers():
    return (Customer.query.order_by(Customer.risk_score.desc())
            .limit(5).all())

# Function for top 5 highest risk scores

def transactions_by_countr():
    results = (db.session.query(Transaction.country, func.count())
               .group_by(Transaction.country).all())
    
    return results

# Function for count of transactions by country

def fraud_by_rule():
    pass

# Function for count of blocked accounts by restriction broken