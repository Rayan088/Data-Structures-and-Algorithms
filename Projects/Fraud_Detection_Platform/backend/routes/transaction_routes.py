from flask import Blueprint, jsonify
from models.transactions import Transaction

transaction_bp = Blueprint("transactions", __name__)

@transaction_bp.route(
    "/api/live-transactions",
    methods=["GET"]
)

def get_live_transactions():
    transactions = (Transaction.query.order_by(
            Transaction.transaction_id.desc()).limit(100).all()
    )

    results = []
    for transaction in transactions:
        results.append(
            {
                "transaction_id": transaction.transaction_id,
                "timestamp": transaction.timestamp.isoformat(),
                "customer_id": transaction.customer_id,
                "amount": transaction.amount,
                "country": transaction.country,
                "device": transaction.device,
                "risk_score": transaction.risk_score,
                "status": transaction.status
            }
        )

    return jsonify(results)