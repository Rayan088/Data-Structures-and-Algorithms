from flask import Blueprint, jsonify
from engines.analytics_engine import AnalyticsEngine

analytics_bp = Blueprint("analytics", __name__)
analytics_engine = AnalyticsEngine()

@analytics_bp.route("/total-transactions")
def total_transactions():
    return jsonify({"total_transactions":
            analytics_engine.total_transactions()
    })

# Total transactions processed

@analytics_bp.route("/high-risk-alerts")
def high_risk_alerts():
    return jsonify({"high_risk_alerts":
            analytics_engine.high_risk_alerts()
    })

# Number of high risk transactions

@analytics_bp.route("/transactions-awaiting-review")
def transactions_awaiting_review():
    return jsonify({"transactions_awaiting_review":
            analytics_engine.transactions_awaiting_review()
    })

# Transactions waiting for analyst review

@analytics_bp.route("/fraud-prevented")
def fraud_prevented():
    return jsonify({"fraud_prevented":
            analytics_engine.fraud_prevented()
    })

# Amount of fraud prevented

@analytics_bp.route("/transactions-by-risk")
def transactions_by_risk():
    results = analytics_engine.transactions_by_risk()

    return jsonify([
        {
            "risk_level": risk,
            "count": count
        }
        for risk, count in results
    ])

# Transactions grouped by risk level

@analytics_bp.route("/riskiest-customers")
def riskiest_customers():
    customers = (analytics_engine.riskiest_customers())

    return jsonify([
        {
            "customer_id":
                customer.customer_id,

            "name":
                customer.name,

            "risk_score":
                customer.risk_score
        }
        for customer in customers
    ])

# Top 5 riskiest customers

@analytics_bp.route("/transactions-by-country")
def transactions_by_country():
    results = (analytics_engine.transactions_by_country())

    return jsonify([
        {
            "country": country,
            "count": count
        }
        for country, count in results
    ])

# Transactions by country

@analytics_bp.route("/fraud-by-rule")
def fraud_by_rule():
    return jsonify(analytics_engine.fraud_by_rule())

# Fraud detection rules breakdown