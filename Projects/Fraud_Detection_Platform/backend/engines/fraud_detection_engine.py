import random

from database.db import db
from models.alert import Alert
from models.customer import Customer
from models.transactions import Transaction

class FraudDetectionEngine:
    def __init__(self, transaction_generator):
        self.transaction_generator = transaction_generator

    # Initializer method

    def process_all_transactions(self):
        customers = {c.customer_id: c for c in Customer.query.all()}

        transactions = (Transaction.query
            .order_by(Transaction.timestamp.asc()).all())

        for transaction in transactions:
            customer = customers.get(
                transaction.customer_id)
            if customer:
                self.analyse_transaction(transaction, customer)

        db.session.commit()

    # Method to process transactions and add to database

    def analyse_transaction(self, transaction):
        customer_profile = (self.transaction_generator.get_customer_profile(transaction.customer_id))

        if not customer_profile:
            return
        
    # Method to get customer profile

    def score_transaction(self, transaction, profile, customer):
        risk_score = random.randint(5, 15)
        reasons = []

        trusted_devices = profile["trusted_devices"]

        if transaction.device not in trusted_devices:
            risk_score += random.randint(7, 17)

            reasons.append("NEW_DEVICE")

        # Checks if device within users trusted devices

        average_amount = profile["avg_amount"]

        if average_amount and transaction.amount > average_amount * 2.5:
            risk_score += random.randint(15, 25)
            reasons.append("HIGH_AMOUNT")

        # Checks if transaction amount is greater than normal

        normal_country = customer.home_country

        if transaction.country != normal_country:
            risk_score += random.randint(17, 24)
            reasons.append("IMPOSSIBLE_TRAVEL")

        # Checks if user wallet is used in different country

        favourite_merchants = (profile["favourite_merchants"])

        if transaction.merchant not in favourite_merchants:
            risk_score += random.randint(14, 18)

            reasons.append("UNFAMILIAR_MERCHANT")

        # Checks if unfamiliar merchant in transaction

        risk_score = min(risk_score, 100)

        transaction.risk_score = risk_score
        transaction.risk_level = (self.calculate_risk_level(risk_score))

        transaction.status = (self.calculate_status(transaction.risk_level))

        customer.risk_score = max(customer.risk_score, risk_score)

        if transaction.status in ["REVIEW", "BLOCKED"]:
            self.create_alert(transaction, reasons)
    
    # Method to score transaction and add to appropriate database

    def calculate_risk_level(self, score):
        if score < 20:
            return "LOW"
        elif score < 45:
            return "MEDIUM"
        elif score < 70:
            return "HIGH"
        else:
            return "CRITICAL"
        
    # Method to calculate risk level

    def calculate_status(self, level):
        if level == "LOW":
            return "APPROVED"
        elif level == "MEDIUM":
            if random.random() < 0.1:
                return "REVIEW"
            return "APPROVED"
        elif level == "HIGH":
            return "REVIEW"
        else:
            return "BLOCKED"
        
    # Method to calculate transaction status

    def create_alert(self, transaction, reasons):
        alert = Alert(
            transaction_id=transaction.transaction_id,
            customer_id=transaction.customer_id,
            risk_score=transaction.risk_score,
            reasons = ", ".join(reasons),
            status=transaction.status)

        db.session.add(alert)

    # Method to add to alert table in database