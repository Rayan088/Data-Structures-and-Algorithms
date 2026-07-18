from flask import Blueprint, jsonify
import json

from database.db import db
from models.customer import Customer
from models.transactions import Transaction
from models.alert import Alert

customer_details = Blueprint("customer_details", __name__)

@customer_details.route("/api/customers/<customer_id>/recent-transactions", methods=["GET"])
def get_recent_transactions(customer_id):
    transactions = (
        Transaction.query.filter_by(customer_id=customer_id)
        .order_by(Transaction.timestamp.desc()).limit(5).all())

    result = [
        {
            "timestamp": txn.timestamp.isoformat(),
            "merchant": txn.merchant,
            "amount": txn.amount,
            "country": txn.country,
            "device": txn.device,
        }
        for txn in transactions
    ]

    return jsonify(result)

# Method to return 5 previous transactions

@customer_details.route("/api/customers/<customer_id>/profile", methods=["GET"])
def get_customer_profile(customer_id):
    customer = Customer.query.filter_by(customer_id=customer_id).first()

    if not customer:
        return jsonify({"error": "Customer not found"}), 404

    avg_spend_result = (
        db.session.query(db.func.avg(Transaction.amount))
        .filter(Transaction.customer_id == customer_id).scalar())

    avg_spend = round(avg_spend_result, 2) if avg_spend_result else 0

    trusted_devices = customer.trusted_devices.split(",") if customer.trusted_devices else []

    profile = {
        "home_country": customer.home_country,
        "trusted_devices": trusted_devices,
        "avg_spend": avg_spend,
    }

    return jsonify(profile)

# Method to return home country, trusted devices and average spend

@customer_details.route("/api/transactions/<transaction_id>/alerts", methods=["GET"])
def get_transaction_alerts(transaction_id):
    alerts = Alert.query.filter_by(transaction_id=transaction_id).all()

    all_rules = []
    for alert in alerts:
        if alert.reasons:
            rules = [r.strip() for r in alert.reasons.split(",")]
            all_rules.extend(rules)

    result = [{"reason": rule} for rule in all_rules]

    return jsonify(result)

# Method to return all rules broken